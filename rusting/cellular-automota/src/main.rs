use macroquad::prelude::*;

pub mod maths;

pub mod board;
use crate::board::Board;

enum UpdateMode {
    Menu,
    Game,
    Pause
}

struct Game {
    update_mode:UpdateMode,
    board: Board,
    camera_pos: Vec2
}

impl Game {
    fn new() -> Self {
        Game {
            update_mode: UpdateMode::Menu,
            board: Board::new(),
            camera_pos: Vec2::ZERO
        }
    }

    async fn menu_update(&mut self) {
        if is_key_pressed(KeyCode::Space) {
            self.update_mode = UpdateMode::Game;
        }

        draw_text("Press Space to Start", screen_width()/4., screen_height()/4., 40., WHITE);
    }

    async fn game_update(&mut self) {
        if is_key_pressed(KeyCode::Escape) {
            self.update_mode = UpdateMode::Pause;
        }
        for key in get_keys_down() {
            match key {
                KeyCode::W=>{self.camera_pos.y -= 1.},
                KeyCode::A=>{self.camera_pos.x -= 1.},
                KeyCode::S=>{self.camera_pos.y += 1.},
                KeyCode::D=>{self.camera_pos.x += 1.},
                _=>{}
            }
        }

        clear_background(GRAY);

        self.board.render(&self.camera_pos);
    }

    async fn pause_update(&mut self) {
        if is_key_pressed(KeyCode::Escape) {
            self.update_mode = UpdateMode::Game;
        }
    }
}

#[macroquad::main("Cellular Automota")]
async fn main() {
    /*----------Inits----------*/
    let mut game = Game::new();

    game.board.rand_fill();
    
    /*----------Loops----------*/
    loop {

        match game.update_mode {
            UpdateMode::Menu => { game.menu_update().await},
            UpdateMode::Game => { game.game_update().await},
            UpdateMode::Pause => { game.pause_update().await}
        }

        next_frame().await
    }
}
