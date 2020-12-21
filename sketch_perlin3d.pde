float t = 0;

void setup(){
  size(600,300,P3D);
 
  fill(255,128);
  noStroke();
  lights();
}

void draw(){
  background(0);
  t++;
  //clear();
  for(int x=0;x<width;x+=20){
    for(int y=0;y<height;y+=20){
      for(int z=40;z<300;z+=20){
        float n =noise(0.02*x,0.02*y,0.02*(z+t));
        translate(x,y,-z);
        fill(255,n*160);
        box(n*25);
        translate(-x,-y,z);
      }
    }
  }
}