use macroquad::prelude::*;

pub enum Forces {
    Vector(Vec2),
    Attraction(f32),
    Repel(f32)
}

pub struct Point {
    x: f32,
    y: f32,
    vx: f32,
    vy: f32,
    radius: f32,
    color: Color
}

pub struct PointManager {
    points: Vec<Point>,

    forces: Forces,
    points_collide: bool,
}

impl PointManager {
    pub fn new(forces: Forces, points_collide: bool) -> Self {
        PointManager {
            points: Vec::new(),
            forces,
            points_collide
        }
    }

    pub fn clear(&mut self) {
        self.points.clear();
    }

    pub fn add_point(&mut self, x: f32, y: f32, radius: f32, color: Color) {
        let point = Point { x, y, vx: 0.0, vy: 0.0, radius, color };
        self.points.push(point);
    }

    pub fn update_points(&mut self) {
        // Update velocities based on gravity
        // for force in self.forces
        //      Vec => apply vec,
        // and  
        match self.gravity {
            Gravity::Vector(vec) => {
                for point in &mut self.points {
                    point.vx += vec.x;
                    point.vy += vec.y;
                }
            },
            Gravity::Strength(strength) => {
                // Snapshot positions so we don't immutably borrow self.points while mutably iterating it
                let positions: Vec<(f32, f32)> = self.points.iter().map(|p| (p.x, p.y)).collect();
                let len = self.points.len();
                let mut accels: Vec<(f32, f32)> = vec![(0.0, 0.0); len];

                // Compute pairwise accelerations into the accumulator
                for i in 0..len {
                    let (xi, yi) = positions[i];
                    for j in 0..len {
                        if i == j {
                            continue;
                        }
                        let (xj, yj) = positions[j];
                        let dx = xj - xi;
                        let dy = yj - yi;
                        let distance_sq = dx * dx + dy * dy;
                        if distance_sq == 0.0 {
                            continue; // avoid division by zero
                        }
                        let distance = distance_sq.sqrt();
                        let force = strength / distance_sq; // inverse square law
                        let ax = force * (dx / distance);
                        let ay = force * (dy / distance);
                        accels[i].0 += ax;
                        accels[i].1 += ay;
                    }
                }

                // Apply accumulated accelerations to velocities
                for (point, accel) in self.points.iter_mut().zip(accels.iter()) {
                    point.vx += accel.0;
                    point.vy += accel.1;
                }
            },
        }

        // Handle collisions with other points
        {
            // First: update positions and handle screen-boundary collisions
            for point in &mut self.points {
                // X-axis
                point.x += point.vx;
                if point.x + point.radius >= screen_width() {
                    point.x = screen_width() - point.radius;
                    point.vx = point.vx * -0.7;
                } else if point.x - point.radius <= 0. {
                    point.x = point.radius;
                    point.vx = point.vx * -0.7;
                }

                // Y-axis
                point.y -= point.vy; // Invert Y for screen coordinates
                if point.y + point.radius >= screen_height() {
                    point.y = screen_height() - point.radius;
                    point.vy = point.vy * -0.7;
                } else if point.y - point.radius <= 0. {
                    point.y = point.radius;
                    point.vy = point.vy * -0.7;
                }
            }

            // Then: handle collisions between points using split_at_mut to get two distinct &mut refs
            if self.points_collide {
                let len = self.points.len();
                for i in 0..len {
                    for j in (i + 1)..len {
                        // split_at_mut gives two non-overlapping slices so we can borrow mutably twice
                        let (left, right) = self.points.split_at_mut(j);
                        let a = &mut left[i];
                        let b = &mut right[0];

                        let dx = b.x - a.x;
                        let dy = b.y - a.y;
                        let distance = (dx * dx + dy * dy).sqrt();

                        // avoid division by zero and only act when overlapping
                        if distance == 0.0 || distance >= a.radius + b.radius {
                            continue;
                        }

                        // normal
                        let nx = dx / distance;
                        let ny = dy / distance;

                        // simple elastic collision assuming equal mass
                        let rvx = a.vx - b.vx;
                        let rvy = a.vy - b.vy;
                        let vel_along_normal = rvx * nx + rvy * ny;

                        // if velocities are separating, skip
                        // if vel_along_normal > 0.0 {
                        //     continue;
                        // }

                        let elasticity = 0.7; // match your boundary bounce
                        let j_impulse = -(1.0 + elasticity) * vel_along_normal / 2.0; // equal mass => divide by 2

                        let ix = j_impulse * nx;
                        let iy = j_impulse * ny;

                        a.vx += ix;
                        a.vy += iy;
                        b.vx -= ix;
                        b.vy -= iy;

                        // positional correction to prevent sinking
                        let penetration = a.radius + b.radius - distance;
                        let percent = 0.2; // usually 20% to 80%
                        let correction = (penetration / 2.0) * percent;
                        let cx = correction * nx;
                        let cy = correction * ny;
                        a.x -= cx;
                        a.y -= cy;
                        b.x += cx;
                        b.y += cy;
                    }
                }
            }
        }
    }

    pub fn set_gravity(&mut self, gravity: Gravity) {
        self.gravity = gravity;
    }

    pub fn draw_points(&self) {
        for point in &self.points {
            draw_circle(point.x, point.y, point.radius, point.color);
        }
    }
    pub fn draw_debug_data(&self) {
        // Draw gravity vector
        let mut grav_vec = Vec2::new(0.,0.);

        match self.gravity {
            Gravity::Vector(vec) => {
                grav_vec = vec;
            },
            Gravity::Strength(strength) => {
                grav_vec = Vec2::new(0., -strength);
            },
        }
        draw_circle(screen_width()/2., screen_height()/2., 5.0, YELLOW);
        draw_line(screen_width()/2., screen_height()/2., screen_width()/2. + grav_vec.x*1000., screen_height()/2. + grav_vec.y*-1000., 1., YELLOW);

        // Draw point velocity vectors
        for point in &self.points {
            draw_line(point.x, point.y, point.x + point.vx*10., point.y - point.vy*10., 1., RED);
            draw_circle(point.x, point.y, 2., RED);
        }
    }
}