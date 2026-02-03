use macroquad::prelude::*;

use crate::{maths::*, physics::Physics};

// enum GeoPrimitive {
//     Rect(Rect),
//     Circle(Circle),
// }

// impl GeoPrimitive {
//     fn collides_with(&self, obj: &GeoPrimitive) {
//         match self {
//             GeoPrimitive::Rect=>{
//                 match obj {
//                     Rect=>{}
//                 }
//             },
//             Circle=>{}
//         }
//     }
// }

struct Entity<'a> {
    shape: GeoPrimitive,
    pos: Vec2,
    vel: Vec2,
    color: Color,
    is_static: bool,
    phys_rules: &'a Physics
}

impl Entity {
    fn collides_with(&self, obj: &Self) {
        
    }
}

trait HasPhysics {
    fn update();
}