import processing.video.*;

float x ;
float y ;
Capture video;

void setup(){
  size(640,480);
  background(0);
  x=width/2;
  y=height/2;
  video = new Capture(this,width,height);
  video.start();
}

void captureEvent(Capture video){
  video.read();
}
  


void draw(){
  video.loadPixels();
  float newx = constrain(x+random(-20,20),0,width-1);
  float newy = constrain(y+random(-20,20),0,height-1);
  
  int midx =int((newx+x)/2);
  int midy = int((newy+y)/2);
  color c=video.pixels[(width-1-midx)+midy*video.width];
  
  stroke(c);
  strokeWeight(0.5);
  line(x,y,newx,newy);
  
  x=newx;
  y=newy;
}