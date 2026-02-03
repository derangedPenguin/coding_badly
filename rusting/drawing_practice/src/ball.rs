use macroquad::prelude::*;

use crate::{maths::*, physics::Physics};

pub struct Ball<'a> {
    pub pos: Vec2,
    pub vel: Vec2,
    pub size: f32,
    pub color: Color,
    pub phys_active: bool,
    pub phys_rules: &'a Physics
}

impl PhysEntity for Ball<'_> {
    fn update(&mut self) {
        if !self.phys_active { return }


        //Gravity
        self.vel.y -= self.phys_rules.gravity;

        //-Motion
        let next_x = self.pos.x + self.vel.x;
        if next_x > 0. + self.size && next_x < screen_width() - self.size {
            self.pos.x = next_x;
        } else {
            self.vel.x *= -0.8;
        }
        self.vel.x = abs_subtract(self.vel.x, self.phys_rules.air_resistance);

        let next_y = self.pos.y - self.vel.y;
        if next_y > 0. + self.size && next_y < screen_height() - self.size {
            self.pos.y = next_y;
        } else {
            self.vel.y *= -0.8;
            if self.vel.y.abs() < 0.1 {self.vel.y = 0.}
            self.vel.x = if self.vel.x.abs() < self.phys_rules.friction {0.} else {(self.vel.x.abs() - self.phys_rules.friction) * self.vel.x.abs() / self.vel.x};
        }
        self.vel.y = abs_subtract(self.vel.y, self.phys_rules.air_resistance);
    }
}

impl RenderEntity for Ball<'_> {
    fn render(&self) {
        draw_circle(self.pos.x, self.pos.y, self.size, self.color);
    }
    fn render_debug_info(&self) {
        draw_text(&format!("vy: {}", self.vel.y), 0., 50., 16., DARKGRAY);
        draw_text(&format!("vx: {}", self.vel.x), 0., 70., 16., DARKGRAY);
    }
}

pub trait PhysEntity {
    fn update(&mut self);
}

pub trait RenderEntity {
    fn render(&self);
    fn render_debug_info(&self);
}

