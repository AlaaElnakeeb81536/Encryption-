#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include<String.h>

int isUpper(char c);
int isLower(char c);
int isNum(char c);

void encryption_message(char m[],unsigned char k);
void decryption_message(char m[],unsigned char k);

#define KEY (5U) //key of the incryption messages

//create an RF24 object
RF24 radio(10, 9);  /* CE: is an active-high pin. When enabled, the nRF24L01 will either transmit or receive, depending on the mode.
                     * CSN: is an active-low pin that is typically held HIGH. When this pin goes low, the nRF24L01 begins listening for data on its SPI port and processes it accordingly.
                     */

//address through which two modules communicate.
const byte address[6] = "00001";

String message= "";
char mess[50] = "Hello World";
int Size_t =0;

void setup()
{
  Serial.begin(9600);
  radio.begin();

  //set the address
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  //Set module as transmitter
  radio.stopListening();
}
void loop()
{
  //Send message to receiver
  encryption_message(mess,KEY);
  radio.write(&mess, Size_t);
  delay(1000);
  while(1)
  {
    Serial.println("Enter your message");
    while (Serial.available() == 0) {}
    message = Serial.readString();
    Serial.println("YOUR Message:" + message);
    for(int i=0;i<message.length();i++)
    {
      mess[i]=message[i];
    }
    //Serial.println(mess);
    encryption_message(mess,KEY);
    //Serial.println(mess);
    radio.write(&mess,Size_t);
  }

}

int isUpper(char c)
{
    int flage=0;
    if( (((int)c)>=65) && (((int)c)<=90) )
    {
        flage=1;
    }
    else
    {
        flage=0;
    }
    return flage;
}

int isLower(char c)
{
    int flage=0;
    if( (((int)c)>=97) && (((int)c) <=122) )
    {
        flage=1;
    }
    else
    {
        flage=0;
    }
    return flage;
}

int isNum(char c)
{
    int flage=0;
    if( ( ((int)c)>=48 )&& (((int)c)<=57) )
    {
        flage=1;
    }
    else
    {
        flage=0;
    }
    return flage;
}

void encryption_message(char m[],unsigned char k)
{
    int temp=0;
    for(int i=0;m[i]!='\0';i++)
    {
        Size_t=Size_t+1;
    }
    for(int i=0;i<Size_t;i++)
    {
        if(isNum(m[i]))
        {
           temp=(int)m[i];
           temp=(temp + k - 48) % 10 + 48;
           mess[i]=(char)temp;
        }
        else if(isUpper(m[i]))
        {
            temp=(int)m[i];
            temp=(temp + k - 65) % 26 + 65;
            mess[i]=(char)temp;
        }
        else if(isLower(m[i]))
        {
            temp=(int)m[i];
            temp=(temp + k - 97) % 26 + 97;
            mess[i]=(char)temp;
        }
    }
}
