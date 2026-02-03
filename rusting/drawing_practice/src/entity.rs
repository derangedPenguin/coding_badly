use macroquad::prelude::*;

use crate::{maths::*, physics::Physics};

struct Entity<'a> {
    pos: Vec2,
    vel:Vec2,
    color: Color,
    is_static: bool,
    physics: &'a Physics
}