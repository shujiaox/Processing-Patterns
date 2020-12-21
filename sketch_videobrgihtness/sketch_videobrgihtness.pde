import processing.video.*;

Capture video;

void captureEvent(Capture video){
  video.read();
}

void setup(){
  size(320,240);
  video = new Capture(this,320,240);
  video.start();
}

void draw(){
  //loadPixels();
  video.loadPixels();
  
  //for(int x =0;x<video.width;x++){
  //  for(int y =0;y<video.height;y++){
      int x =int(random(video.width));
      int y =int(random(video.height));
      int loc =x+y*video.width;
      
      float r =red(video.pixels[loc]);
      float g =green(video.pixels[loc]);
      float b =blue(video.pixels[loc]);
      
      
      //float d =dist(x,y,mouseX,mouseY);
      //float adjustbrightness=map(d,0,100,4,0);
      //r *= adjustbrightness;
      //g *= adjustbrightness;
      //b *= adjustbrightness;
      
      //r = constrain(r,0,255);
      //b = constrain(b,0,255);
      //g = constrain(g,0,255);
      
      color c =color(r,g,b);
      //pixels[loc]=c;
      noStroke();
      fill(c,100);
      ellipse(x,y,15,15);
      //updatePixels();
}
      
      
      
    