float t = 0;
float toff = 0.01;

void setup(){
  size(500,500);
  frameRate(15);
}

void draw(){
  background(0);
  noStroke();
  for(int i =0;i<width;i+=50){
    for(int j=0;j<height;j+=50){
      float n = map(noise(t+toff),0,1,10,50);
      fill(random(50,200),2*n,5*n);
      ellipse(i,j,n,n);
      
      t += random(0.001,0.005);
      toff += random(0.001,0.005);}
    }
  }
      