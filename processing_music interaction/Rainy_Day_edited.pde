import processing.sound.*;



//sound files
SoundFile mySound;
SoundFile mySound2;
SoundFile mySound3;
SoundFile mySound4;
SoundFile mySound5;

void setup() {
  frameRate(10);
  size(2000, 1500);
  background(50);

  //five kinds of sound
  mySound  = new SoundFile(this,"music01.mp3");
  mySound2  = new SoundFile(this,"music02.mp3");
  mySound3  = new SoundFile(this,"music03.mp3");
  mySound4  = new SoundFile(this,"music04.mp3");
  mySound5  = new SoundFile(this,"music05.mp3");

}

void draw() {
  background(50);
  noFill();

  for (int i =-4; i<5; i=i+1) {
    //press key 'a',the first rain appears
    if (mySound.isPlaying()) {
      fill(#FF7979);
      stroke(255);
      int X1= int(i*15+width/6);
      rect(X1, 0, random(8, 12), random(50, height));
    }

    //press key 'd',the second rain appears
    if (mySound2.isPlaying()) {
      fill(#91D6A6);
      stroke(255);
      int X2= int(i*15+width*2/6);
      rect(X2, 0, random(8, 12), random(50, height));
    }

    //press key 'g',the third rain appears
    if (mySound3.isPlaying()) {
      fill(#FAF8B3);
      stroke(255);
      int X3= int(i*15+width*3/6);
      rect(X3, 0, random(8, 12), random(50, height));
    }

    //press key'j',the forth rain appears
    if (mySound4.isPlaying()) {
      fill(#B3DFFA);
      stroke(255);
      int X4= int(i*15+width*4/6);
      rect(X4, 0, random(8, 12), random(50, height));
    }

    //press key'l',the last rain appears
    if (mySound5.isPlaying()) {
      fill(255);
      stroke(255);
      int X5= int(i*15+width*5/6);
      rect(X5, 0, random(8, 12), random(50, height));
    }
  }
}
  //sound only appears once when press the button

  void keyPressed() {

    if (key == 'a') {
      mySound.play();
      //mySound.stop();
      mySound2.stop();
      mySound3.stop();
      mySound4.stop();
      mySound5.stop();
    }
    if (key == 'd') {
      mySound2.play();
      mySound.stop();
      //mySound2.stop();
      mySound3.stop();
      mySound4.stop();
      mySound5.stop();
    }
    if (key == 'g') {
      mySound3.play();
      mySound.stop();
      mySound2.stop();
      //mySound3.stop();
      mySound4.stop();
      mySound5.stop();
    }
    if (key == 'j') {
      mySound4.play();
      mySound.stop();
      mySound2.stop();
      mySound3.stop();
      //mySound4.stop();
      mySound5.stop();
    }
    if (key == 'l') {
      mySound5.play();
      mySound.stop();
      mySound2.stop();
      mySound3.stop();
      mySound4.stop();
      //mySound5.stop();
    }
  }