#[derive(PartialEq, Eq, Hash, Clone, Copy)]
pub struct Point {
    x: i32,
    y: i32
}
impl Point {
    pub fn new(x: i32, y: i32) -> Self {
        Point {
            x: x,
            y: y
        }
    }
}

