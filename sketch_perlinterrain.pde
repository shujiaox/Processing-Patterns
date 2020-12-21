int density =20;//改变地形平缓度
int cols,rows;
int w = 2000;
int h = 1600;
float[][]terrain;//二维矩阵存贮变化点
float jump = 0;


void setup(){
  size(600,600,P3D);
  cols = w/density;
  rows = h/density;
  terrain = new float[cols][rows];
}

void draw(){
  jump -= 0.1;
  float yoff = jump;
  
  for(int y=0;y<rows;y++){
    float xoff = 0;
    for(int x=0;x<cols;x++){
      terrain[x][y]=map(noise(xoff,yoff),0,1,-100,100);
      xoff += 0.2;}
      yoff += 0.2;}
      
  background(0);
  stroke(255);
  noFill();
  translate(width/2,height/2+50);
  rotateX(PI/3);
  translate(-w/2,-h/2);
  
  for(int y=0;y<rows-1;y++){
    beginShape(TRIANGLE_STRIP);
    for(int x=0;x<cols;x++){
      vertex(x*density,y*density,terrain[x][y]);
      vertex(x*density,(y+1)*density,terrain[x][y+1]);
    }
    endShape();
  }
 }