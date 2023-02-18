//Include Libraries
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define KEY (5U)

int isUpper(char c);
int isLower(char c);
int isNum(char c);

void decryption_message(char m[],unsigned char k);

char mess[50]="";
int Size_t =0;

//create an RF24 object
RF24 radio(10, 9);  // CE, CSN

//address through which two modules communicate.
const byte address[6] = "00001";

void setup()
{
  while (!Serial);
    Serial.begin(9600);

  radio.begin();

  //set the address
   radio.openReadingPipe(0, address);
   radio.setPALevel(RF24_PA_MIN);
  //Set module as receiver
   radio.startListening();
}

void loop()
{
  //Read the data if available in buffer
  if (radio.available())
  {
    radio.read(&mess,sizeof(mess));     // recieve the message
    decryption_message(mess,KEY); // encrypte the message
    for(int i=0;i<Size_t;i++)     // print the real message on monitor screen
    {
      Serial.print(mess[i]);
    }
    Serial.print("\n");
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

void decryption_message(char m[],unsigned char k)
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
           if((temp - k - 48)>=0)
           {
                temp=(temp - k - 48) % 10 + 48;
           }
           else
           {
                temp=temp + k;
           }
           mess[i]=(char)temp;
        }

        else if(isUpper(m[i]))
        {
            temp=(int)m[i];
            if((temp - k - 65)>=0)
            {
                temp=(temp - k - 65) % 26 + 65;
            }
            else
            {
                temp=91+(temp - k - 65);
            }
            mess[i]=(char)temp;
        }
        else if(isLower(m[i]))
        {
            temp=(int)m[i];
            if((temp - k - 97)>=0)
            {
                temp=(temp - k - 97) % 26 + 97;
            }
            else
            {
                temp=123+(temp - k - 97);
            }
            mess[i]=(char)temp;
        }
    }
}
