int button_pin = A0;

void setup()
{
    Serial.begin(9600);
    pinMode(button_pin, INPUT);
}

bool last_button = false;
void loop()
{
    bool button = digitalRead(button_pin);
    if (last_button != button)
    {
        if (button) {
            Serial.println("Cool");
        }
        delay(100);
    }
    last_button = button;
}
