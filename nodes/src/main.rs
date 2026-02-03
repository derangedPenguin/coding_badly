use macroquad::prelude::*;

pub mod pointManager;
use crate::pointManager::{Point, PointManager};


#[macroquad::main("Node-ing off")]
async fn main() {
    // Init Code
    let mut point_mngr = PointManager::new();
    

    // Loops
    loop {
        clear_background(Color { r: 0.8, g: 0.8, b: 0.8, a: 1.0 });

        if is_mouse_button_pressed(MouseButton::Left) {
            point_mngr.add_point(Point::new(mouse_position().0, mouse_position().1, 10.0, SKYBLUE));
        }

        point_mngr.render();

        next_frame().await
    }
}
