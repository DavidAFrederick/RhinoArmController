#include <Wire.h>
#define SLAVE_ADDRESS 0x08

int data_to_echo = 0;
int received_command = 0;
int command_response = 0;


const int array_size = 33;
int received_data_array[array_size];
int send_data_array[array_size];
int length_of_send_data_array;
int last_command_received = 0;

int IF_A_status = 0;
int IF_B_status = 0;
int IF_C_status = 0;
int IF_D_status = 0;
int IF_E_status = 0;
int IF_F_status = 0;

int IF_A_count_status = 1023;
int IF_B_count_status = 2047;
int IF_C_count_status = 4095;
int IF_D_count_status = 0;
int IF_E_count_status = 0;
int IF_F_count_status = 0;



void setup()
{
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(sendDataEvent);

  Serial.begin(9600);
  Serial.println(F(""));
  Serial.println(F(">> Restarting "));
}
//------------------------------------------
void loop() {
  delay (1000);
  IF_A_count_status = IF_A_count_status + 1;
  IF_B_count_status = IF_B_count_status + 1;
  IF_C_count_status = IF_C_count_status + 1;

    Serial.print("IF_A_count_status:  ");
    Serial.print(IF_A_count_status);
    Serial.print("    IF_B_count_status:  ");
    Serial.print(IF_B_count_status);
    Serial.print("    IF_C_count_status:  ");
    Serial.println(IF_C_count_status);

  
}
//------------------------------------------
void receiveEvent(int rx_byte_count)
{
  //  Serial.print("CMD bytes received:  ");
  //  Serial.println(rx_byte_count);

  for (int i = 0; i < array_size; i++) {    // Clear out old data
    received_data_array[i] = 0;
  }

  for (int i = 0; i < rx_byte_count; i++)  {
    received_data_array[i] = Wire.read();
  }

  if (rx_byte_count > 1) {
    length_of_send_data_array = received_data_array[rx_byte_count - 1]; //  The last byte is the response size
    Serial.print(" Exit RX   Response size: ");
    Serial.println(length_of_send_data_array);
  }


  for (int i = 0; i < rx_byte_count; i++)  {
    Serial.print(received_data_array[i]);   //check what you are receiving against an Intel-Hex frame
    Serial.print ("R");
  }
  
  Serial.println ("|");

  if (received_data_array[1] != 0){
    last_command_received = received_data_array[1];
    Serial.print ("Last CMD: ");
    Serial.println (last_command_received);
    }

  if (received_data_array[1] == 11){
    int angle = received_data_array[2];
    Serial.print ("Angle: "); Serial.println (angle);
    IF_A_status = IF_A_status + 1;
    if (IF_A_status == 3){ 
      IF_A_status = 0;
      };
  }


  if (received_data_array[1] == 50){
//    IF_A_count_status_high_byte = IF_A_count_status / 256;
//    IF_A_count_status_low_byte  = IF_A_count_status % 256;

    
//    Serial.println ("Requesting all counts");
//    Serial.print ("A: "); Serial.println (IF_A_count_status);
//    Serial.print ("B: "); Serial.println (IF_B_count_status);
//    Serial.print ("C: "); Serial.println (IF_C_count_status);
  }


}

//
//------------------------------------------
void sendDataEvent()
{
  for (int i = 0; i < array_size; i++) {    // Clear out old data
    send_data_array[i] = 0;
  }

  send_data_array[0] = 0;
  send_data_array[1] = 1;
  send_data_array[2] = 2;
  send_data_array[3] = 3;
  send_data_array[4] = 4;
  send_data_array[5] = 5;
  send_data_array[6] = 6;
//  send_data_array[7] = 7;
//  send_data_array[8] = 8;
//  send_data_array[9] = 9;
//  send_data_array[10] = 10;
//  send_data_array[11] = 11;
//  send_data_array[12] = 12;
//  send_data_array[13] = 13;
//  send_data_array[14] = 14;
//  send_data_array[15] = 15;
//  send_data_array[16] = 16;
//  send_data_array[17] = 17;
//  send_data_array[18] = 18;
//  send_data_array[19] = 19;
//  send_data_array[20] = 20;


//  Serial.print ("Last CMD: ");
//  Serial.println (last_command_received);

  if (last_command_received == 11){
    send_data_array[length_of_send_data_array - 1] = IF_A_status;
//    Serial.print ("IFA: ");
//    Serial.println (IF_A_status );
  //  Serial.print ("IF_A_status: ");
  //  Serial.println (send_data_array[length_of_send_data_array - 1] );
  //  Serial.print ("Length of response: ");
  //  Serial.println (length_of_send_data_array);
  }

  if (last_command_received == 50){
//    Serial.println ("Requesting all counts");
//    Serial.print ("A:: "); Serial.println (IF_A_count_status);
//    Serial.print ("B:: "); Serial.println (IF_B_count_status);
//    Serial.print ("C:: "); Serial.println (IF_C_count_status);
//    send_data_array[0] = 10;

    send_data_array[0] = IF_A_count_status / 256;   //  IF_A_count_status_high_byte
    send_data_array[1] = IF_A_count_status % 256;   //  IF_A_count_status_low_byte
    
    send_data_array[2] = IF_B_count_status / 256;   //  IF_A_count_status_high_byte
    send_data_array[3] = IF_B_count_status % 256;   //  IF_A_count_status_low_byte

    send_data_array[4] = IF_C_count_status / 256;   //  IF_A_count_status_high_byte
    send_data_array[5] = IF_C_count_status % 256;   //  IF_A_count_status_low_byte


    for (int i = 0; i < length_of_send_data_array; i++)
    {
      Wire.write(send_data_array[i]);
    }

  }


}  // end of Send Data Event
//------------------------------------------
