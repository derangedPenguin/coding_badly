pub fn abs_subtract(a: f32, b: f32) -> f32 {
    if a.abs() < b {
        return 0.
    } else {
        return a - (b * a.abs() / a)
    };
}

trait GeoPrimitive {
    fn collides_with<T: GeoPrimitive>(&self, obj: &T);
}

struct Circle {
    x:f32,
    y:f32,
    r:f32
}
impl GeoPrimitive for Circle {
    fn collides_with<T: GeoPrimitive>(&self, obj: &T) {
        
    }
}
struct Square {
    x:f32,
    y:f32,
    s:f32
}
struct Rect {
    x:f32,
    y:f32,
    w:f32,
    h:f32
}