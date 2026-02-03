use macroquad::prelude::*;

pub mod point_manager;
use crate::point_manager::{Point, PointManager, Gravity};

#[macroquad::main("Drawing Practice")]
async fn main() {
    const ENABLE_DEBUG: bool = true;
    //--Inits
    let mut pm = PointManager::new(Gravity::Vector(Vec2::new(0.0, -0.05)), true);


    // let mut targeting = true;//argetingMode::Inactive;
    let mut last_click_pos = (0.,0.);

    //starter loop
    loop {
        if get_keys_down().len() > 0 {
            break
        }
        draw_text("Press Any Button to Start", screen_width()/4., screen_height()/4., 40., WHITE);
        next_frame().await
    }

    //game loop
    loop {
        //--Input
        for key in get_keys_down() {
            match key {
                KeyCode::Space=>{ pm.update_points();},
                _=>()
            }
        }
        for key in get_keys_pressed() {
            match key {
                KeyCode::A=>{ pm.set_gravity(Gravity::Vector(Vec2::new(-0.05, 0.0))); },
                KeyCode::D=>{ pm.set_gravity(Gravity::Vector(Vec2::new(0.05, 0.0))); },
                KeyCode::W=>{ pm.set_gravity(Gravity::Vector(Vec2::new(0.0, 0.05))); },
                KeyCode::S=>{ pm.set_gravity(Gravity::Vector(Vec2::new(0.0, -0.05))); },
                KeyCode::Right=>{ pm.update_points();},

                KeyCode::R=>{ pm.clear(); },
                _=>()
            }
        }

        if is_mouse_button_pressed(MouseButton::Left) {
            // guy.phys_active = false;
            last_click_pos = mouse_position();
            // (guy.pos.x, guy.pos.y) = last_click_pos;
            // println!("Click at: {:?}", last_click_pos);
            pm.add_point(last_click_pos.0, last_click_pos.1, 20.0, Color { r: 1.0, g: 1.0, b: 1.0, a: 0.3 });
        }
        if is_mouse_button_released(MouseButton::Left) {
            // guy.vel.x = (last_click_pos.0 - mouse_position().0) * 0.05;
            // guy.vel.y = (last_click_pos.1 - mouse_position().1) * -0.05;
            // guy.phys_active = true;
        }

        //--Game Updates
        // pm.update_points();

       //--Rendering
        clear_background(Color::new(0.2, 0.5, 0.3, 1.0));
        pm.draw_points();

        //-Entities
        // guy.render();
        // if !guy.phys_active {
        //     draw_line(last_click_pos.0, last_click_pos.1, mouse_position().0, mouse_position().1, 1., BLACK);
        // }

        //-Debug
        if ENABLE_DEBUG {
            draw_fps();
            pm.draw_debug_data();
        }

        //--Finalize frame
        next_frame().await
    }
}