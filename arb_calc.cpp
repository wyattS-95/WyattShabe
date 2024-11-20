#include <iostream>
#include <string>
#include <iomanip>
#include <cmath> 
/* using cmath for abs function which calculates the 
absolute value of a number which is numbers value without
regard to its sign. ex -150 is 150 */

using namespace std;

int main(){
    double favored, underdog;

    cout << "Enter odds for favored: ";
    cin >> favored;

    cout << "Enter odds for underdog: ";
    cin >> underdog;

    bool isFavoredPos = favored > 0;
    bool isUnderPos = underdog > 0;

    // calc payouts
    double favoredPayout, underPayout;

    if (isFavoredPos) {
        favoredPayout = favored / 100.0;
    } else {
        favoredPayout = 100.0 / abs(favored);
    }

    if (isUnderPos) {
        underPayout = underdog / 100.0;
    } else {
        underPayout = 100.0 / abs(underdog);
    }

    // calc stake amount to ensure no negative profits
    // 1 for over and 0.5 for under works for most soccer games
    double favoredStake = 1 / (favoredPayout + underPayout);
    double underStake = 0.8 / (favoredPayout + underPayout);

    /* adjust the stakes to make sure total investment and 
    potential profits are correct */
    favoredStake *= 10.0; // scale  
    underStake *= 10.0; // scale 
    
    // calc total investment
    double totalInvest = favoredStake + underStake;

    cout << fixed << setprecision(2);
    cout << "\nBet on favored: $" << favoredStake << endl;
    cout << "Bet on underdog: $" << underStake << endl;
    cout << "Total investment: $" << totalInvest << endl << endl;

    // calc profit of each outcome
    double favoredWin = (favoredStake * favoredPayout);
    double underWin = (underStake * underPayout);

    // calc payout for each outcome
    double favoredWinPayout = favoredWin + favoredStake;
    double underWinPayout = underWin + underStake;

    cout << "Payout if favored wins: $" << favoredWinPayout << endl;
    cout << "Payout if underdog wins: $" << underWinPayout << endl << endl;

    // Profits for each outcome
    double favoredProf = (favoredWinPayout - totalInvest);
    double underProf = (underWinPayout - totalInvest);

    cout << "Profit if favored wins: $" << favoredProf << endl;
    cout << "Profit if underdog wins: $" << underProf << endl;

    return 0;
}