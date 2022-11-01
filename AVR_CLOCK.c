#include <avr/io.h>
#include <avr/interrupt.h>



//count the number of overflows for seconds
volatile uint8_t tot_overflow;

//count the number of overflows for sampling the display
volatile uint8_t display_overflow;

//button stances
volatile uint8_t button_down_m;
volatile uint8_t button_down_h;


///var declaration display

int sec =0;
int mins=59;
int hours=0;


  
int first_digit_h ;
int second_digit_h;
int first_digit_m;
int second_digit_m;




void display_c(char number);
void increment_t();
int decode();
void timer1_init();
void debounce_h();
void debounce_m();

int main(){


//// DISPLAY INIT
DDRB=B00001111;
PORTB=PORTB | B00001111;	
//// NR AFISATE
///VAL B-GFEDCBA
DDRD=B11111111;
PORTD=PORTD | B01111111;	
 
///TIMER INTRERUPT
timer1_init();  
  
while (true){
debounce_m() ;   
debounce_h() ;   
if (button_down_m)
{
// Clear flag
button_down_m = 0;

mins++;
}
if (button_down_h)
{
// Clear flag
button_down_h = 0;

if (hours<11){
hours++;
}
else {
  hours=0;
}
}   

}

    return 0;
}


void increment_t() {
	if(sec==60){
sec=0;
mins+=1 ;
}
	if(mins==60){
mins=0;
hours+=1 ;
}
	if(hours==11 and mins==60){
hours=0;
};
};


int decode(int value){
	int first_digit;
	int second_digit;

first_digit=value/10; /// -returneaza partea intreaga
second_digit=value%10; ///-returneaza restul 

return first_digit,second_digit;


}



void timer1_init()
{
    // set up timer with prescaler = 8
    TCCR1B |= (1 << CS10);
  
    // initialize counter
    TCNT1 = 0;
  
    // enable overflow interrupt
    TIMSK1 |= (1 << TOIE1);
  
    // enable global interrupts
    sei();
  
    // initialize overflow counter variable
    tot_overflow = 0;
}
  
// TIMER1 overflow interrupt service routine
// called whenever TCNT1 overflows
ISR(TIMER1_OVF_vect)
{
    // keep a track of number of overflows
    tot_overflow++;
    display_overflow++;
    increment_t();
    first_digit_h=hours/10;
    second_digit_h=hours%10;
    first_digit_m=mins/10;
    second_digit_m=mins%10;	
    // check for number of overflows here itself
    // 31 overflows = 1 seconds delay 
    if (tot_overflow >= 248) 
    {
	sec++;
  
        tot_overflow = 0;   // reset overflow counter
    }



    if (display_overflow >= 0 && display_overflow <= 1) 
    {
	    PORTB=PORTB & B00000000;
    	    PORTB=PORTB | B00001110;
  	    display_c(first_digit_h);
        
    }

    if (display_overflow >=2 && display_overflow <= 3) 
    {
            PORTB=PORTB & B00000000;
    	    PORTB=PORTB | B00001101;
	    display_c(second_digit_h);		
    }
    if (display_overflow >= 4 && display_overflow <= 5) 
    {
	    PORTB=PORTB & B00000000;
    	    PORTB=PORTB | B00001011;
	    display_c(first_digit_m);
    }
    if (display_overflow >= 6 && display_overflow <=6) 
    {
            PORTB=PORTB & B00000000;
    	    PORTB=PORTB | B00000111;	
  	    display_c(second_digit_m);	
        display_overflow = 0;   // reset overflow counter
    }

}


void debounce_m(){

static uint8_t count_m = 0;
static uint8_t button_state_m = 0;
uint8_t current_state_m = (~PINB & (1<<PB4)) != 0;

      if (current_state_m != button_state_m) {
      // Button state is about to be changed, increase counter
      count_m++;
      if (count_m >= 4) {
      // The button have not bounced for four checks, change state
        button_state_m = current_state_m;
      // If the button was pressed (not released), tell main so
        if (current_state_m != 0) {
        button_down_m = 1;
        }
      count_m = 0;
      }
      }  else {
// Reset counter
    count_m = 0;
    }

    }



void debounce_h(){

static uint8_t count_h = 0;
static uint8_t button_state_h = 0;
uint8_t current_state_h = (~PINB & (1<<PB5)) != 0;

      if (current_state_h != button_state_h) {
      // Button state is about to be changed, increase counter
      count_h++;
      if (count_h >= 4) {
      // The button have not bounced for four checks, change state
        button_state_h = current_state_h;
      // If the button was pressed (not released), tell main so
        if (current_state_h != 0) {
        button_down_h = 1;
        }
      count_h = 0;
      }
      }  else {
// Reset counter
    count_h = 0;
    }

    }

void display_c(char number){
switch (number){
  case 0 : 
    PORTD=PORTD & B00000000;
    PORTD=PORTD | B01000000;
    break;
  case 1 : 
    PORTD=PORTD & B00000000;
    PORTD=PORTD | B01111001;
    break;
  case 2 :
    PORTD=PORTD & B00000000; 
    PORTD=PORTD | B00100100;
    break;
  case 3 : 
    PORTD=PORTD & B00000000;
    PORTD=PORTD | B00110000;
    break;
  case 4 : 
    PORTD=PORTD & B00000000;
    PORTD=PORTD | B00011001;
    break;
  case 5 : 
    PORTD=PORTD & B00000000;
    PORTD=PORTD | B00010010;
    break;
  case 6 : 
    PORTD=PORTD & B00000000;
    PORTD=PORTD | B00000010;
    break;    
  case 7 : 
    PORTD=PORTD & B00000000;
    PORTD=PORTD | B01111000;
    break;  
  case 8 : 
    PORTD=PORTD & B00000000;
    PORTD=PORTD | B00000000;
    break;  
  case 9 :
    PORTD=PORTD & B00000000; 
    PORTD=PORTD | B00010000;
    break;  
  case 10 :
    PORTD=PORTD & B00000000;
}


}
