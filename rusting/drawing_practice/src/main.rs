use macroquad::prelude::*;

pub mod ball;
use crate::ball::*;

pub mod entity;

pub mod maths;

pub mod physics;
use crate::physics::Physics;

#[macroquad::main("Drawing Practice")]
async fn main() {
    //--Inits
    let phys = Physics {
        gravity: 0.02,
        friction: 0.02,
        air_resistance: 0.0001
    };

    let mut guy = Ball {
        pos: Vec2::new(250f32, 50f32),
        vel: Vec2::new(0f32, 0f32),
        size: 15.,
        color: RED,
        phys_active: true,
        phys_rules: &phys
    };

    // let mut targeting = true;//argetingMode::Inactive;
    let mut last_click_pos = (0.,0.);

    //starter loop
    loop {
        if is_key_pressed(KeyCode::Space) {
            break
        }
        draw_text("Press Space to Start", screen_width()/4., screen_height()/4., 40., WHITE);
        next_frame().await
    }

    //game loop
    loop {
        //--Input
        for key in get_keys_down() {
            match key {
                KeyCode::A=>{ guy.vel.x -= 0.05 },
                KeyCode::D=>{ guy.vel.x += 0.05 },
                _=>()
            }
        }
        for key in get_keys_pressed() {
            match key {
                KeyCode::Space=>{ guy.vel.y = 1. },
                _=>()
            }
        }

        if is_mouse_button_pressed(MouseButton::Left) {
            guy.phys_active = false;
            last_click_pos = mouse_position();
            (guy.pos.x, guy.pos.y) = last_click_pos;
        }
        if is_mouse_button_released(MouseButton::Left) {
            guy.vel.x = (last_click_pos.0 - mouse_position().0) * 0.05;
            guy.vel.y = (last_click_pos.1 - mouse_position().1) * -0.05;
            guy.phys_active = true;
        }

        //--Game Updates
        //-Physics
        guy.update();

       //--Rendering
        clear_background(Color::new(0.2, 0.5, 0.3, 1.0));

        //-Entities
        guy.render();
        if !guy.phys_active {
            draw_line(last_click_pos.0, last_click_pos.1, mouse_position().0, mouse_position().1, 1., BLACK);
        }

        //-Debug
        draw_fps();
        guy.render_debug_info();

        //--Finalize frame
        next_frame().await
    }
}