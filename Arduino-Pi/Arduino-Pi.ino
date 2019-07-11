float true_times = 0;
float tmp = 1000000;
float times;
float last_times;

int rand_x_int;
float rand_x_float;


int rand_y_int;
float rand_y_float;

float xxyy_tmp;

float p;
float pi;
float pi100;

float float_limit = 16777216.00;
float float_limit_plus = float_limit + 1.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  randomSeed(analogRead(0)); // 未接続ピンのノイズを利用

  float_limit_plus = float_limit_plus + 1.0;
  Serial.println(float_limit);
  Serial.println(float_limit_plus);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  rand_x_int = random(-10000,10001);
  rand_x_float = (float)rand_x_int / 1.0;

  rand_y_int = random(-10000,10001);
  rand_y_float = (float)rand_y_int / 1.0;

  
  xxyy_tmp = rand_x_float * rand_x_float + rand_y_float * rand_y_float;
  

  if (xxyy_tmp <= 1000000.0){
      true_times = true_times + 1;
  }

  last_times = times;
  times = times + 1;

  if (times == last_times){ //Arduinoの不具合対策
    times = times + 2.0;
  }
  
  //
  if (tmp == 1000000){
    p = true_times / times;
    pi = p * 4;
    pi100 = pi * 10000;

    Serial.println(true_times);
    Serial.println(times);
    Serial.println(pi100);
    Serial.println(pi);
    Serial.println("-----");

    tmp = 0;
  }

  tmp = tmp + 1;

  
}
