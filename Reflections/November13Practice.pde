int x = 0; 
void setup() {
  size(600, 600);
  background(127);
  frameRate(20);
}
void draw() {
  background(127);
  rect(x, 100, 100, 400);
  x = x + 5; 
}
