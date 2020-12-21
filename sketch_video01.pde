import processing.video.*;
Capture video;
PImage prevFrame;
float threshold = 80;


void setup(){
  size(640,480);
  video = new Capture(this,width,height,30);
  video.start();
  prevFrame = createImage(video.width,video.height,RGB);
}

void captureEvent(Capture video){
  prevFrame.copy(video,0,0,video.width,video.height,
                 0,0,video.width,video.height);
  prevFrame.updatePixels();
  video.read();
}

void draw(){
  loadPixels();
  video.loadPixels();
  prevFrame.loadPixels();
  
  //image(video,0,0);aaaa`
  
  for(int x =0;x<video.width;x++){
    for(int y=0;y<video.height;y++){
      int loc =x+y*video.width;
      
      
      color current =video.pixels[loc];
      color previous =prevFrame.pixels[loc];
      //比较前景图和后景图
      float r1=red(current);
      float g1=green(current);
      float b1=blue(current);
      float r2=red(previous);
      float g2=green(previous);
      float b2=blue(previous);
      float diff = dist(r1,g1,b1,r2,g2,b2);
      
      if(diff>threshold){
        pixels[loc]=color(0);
      }
      else{
        pixels[loc]=color(255);
      }
    }
  }
  updatePixels();
}


//void mousePressed(){
//  backgroundImage.copy(video,0,0,video.width,video.height,
//                       0,0,video.width,video.height);
//  backgroundImage.updatePixels();
//}