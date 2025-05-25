#include <iostream>
using namespace std;
char input;
int user{0},comp{0};

void computer(int comp){
    if (comp == 1){
        cout<< "Computer throws Rock"<<endl;
    }else if(comp == 2){
        cout << "Computer throws Paper"<<endl;

    }else if(comp == 3){
        cout << "Computer throws Scissors"<<endl;
    }
}
int main(){
cout<<"Do you want to play Rock, Paper, Scissors? Type 'y' for yes, 'n' for no";
cin>> input;
while(input=='y'){
    comp= 1 + (rand() % 3);
    cout<< "Please choose Rock(1), Paper(2), or Scissors(3): \n";
    cin >> user;
    
    if(comp == 1){
        cout<< "Computer throws Rock"<<endl;
        if(user == 1){
            cout<< "It's a tie!"<<endl;
        }
        else if(user == 3){
            cout<< "Computer wins!"<<endl;
        }
        else if(user == 2){
            cout<< "You win!"<<endl;
        }
    }
    else if(comp == 2){
        cout << "Computer throws Paper"<<endl;
        if(user == 1){
            cout<< "Computer wins!"<<endl;
        }
        else if(user == 2){
            cout<< "It's a tie!"<<endl;
        }
        else if(user ==  3){
            cout<< "You win!"<<endl;
        }
    }
    else if(comp == 3){
        cout << "Computer throws Scissors"<<endl;
        if(user == 1){
            cout<< "You win!"<<endl;
        }
        else if(user == 2){
            cout<< "Computer wins!"<<endl;
        }
        else if(user == 3){
            cout<< "It's a tie!"<<endl;
        }
    }

    cout<<"Do you want to play again? (y/n)";
    cin>>input;
    }
    cout<< "Thanks for playing";
}
