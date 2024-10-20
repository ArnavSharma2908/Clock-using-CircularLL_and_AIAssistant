#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct Clock {
    Node* hour;
    Node* minute;
    Node* second;
    int flag;  // 0 for AM, 1 for PM
} Clock;


Node* append(Node* start, int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    if (start == NULL) {
        start = newNode;
        newNode->next = start;
    } else {
        Node* end = start;
        while (end->next != start) {
            end = end->next;
        }
        end->next = newNode;
        newNode->next = start;
    }
    return start;
}

void tick_hour(Clock* clk) {
    if (clk->hour->data == 11) {
        clk->flag = !clk->flag;  // Toggle AM/PM
    }
    clk->hour = clk->hour->next;
}

void tick_minute(Clock* clk) {
    if (clk->minute->data == 59) {
        tick_hour(clk);
    }
    clk->minute = clk->minute->next;
}


void tick(Clock* clk) {
    if (clk->second->data == 59) {
        tick_minute(clk);
    }
    clk->second = clk->second->next;
}


void print_clock(Clock* clk) {
    const char* meridium[] = {"AM", "PM"};
    printf("%02d:%02d:%02d %s\n", clk->hour->data, clk->minute->data, clk->second->data, meridium[clk->flag]);
}


Clock* create_CLL() {
    Clock* clk = (Clock*)malloc(sizeof(Clock));
    clk->flag = 0;  // Start with AM

    Node* secondStart = NULL;
    Node* minuteStart = NULL;
    Node* hourStart = NULL;

    // Create circular linked list for minutes and seconds (0-59)
    for (int i = 0; i < 60; i++) {
        minuteStart = append(minuteStart, i);
    }
    secondStart = minuteStart;  // Copy the list for seconds

    // Create circular linked list for hours (1-12)
    for (int i = 1; i <= 12; i++) {
        hourStart = append(hourStart, i);
    }

    clk->hour = hourStart;
    clk->minute = minuteStart;
    clk->second = secondStart;

    return clk;
}

int main() {
    // Create the clock object
    Clock* Time_Obj1 = create_CLL();
    
    // Simulate ticking the clock 120 times (2 minutes)
    for (int i = 0; i < 10000; i++) {
        tick(Time_Obj1);
    }
    print_clock(Time_Obj1);

    return 0;
}
