use std::collections::HashMap;

use macroquad::prelude::*;

pub struct Point {
    x:f32,
    y:f32,
    r:f32,
    color:Color
}
impl Point {
    pub fn new(x:f32, y:f32, r:f32, color:Color) -> Point {
        Point { x, y, r, color }
    }
}

pub struct PointManager {
    pub points: Vec<Point>
}

impl PointManager {
    pub fn new() -> PointManager {
        PointManager {points: vec![]}
    }
    pub fn add_point(&mut self, point:Point) {
        self.points.push( point );
    }
    pub fn render(&self) {
        for point in self.points.iter() {
            draw_circle(point.x, point.y, point.r, point.color);
        }
    }
}