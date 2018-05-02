#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<ll> vl;
typedef vector< vector<ll> > vvl;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define FOR(i, a, b) \
for (int i = (a); i < (b); i++)
#define FORE(i, a, b) \
for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) \
for (int i = (a); i >= (b); i--)

#define INF 2e9 // 2e9
#define INFLL 2e18 // 2e18
#define esp 1e-9
#define PI 3.14159265

inline ll GCD(ll a, ll b) {while (b != 0) {ll c = a % b; a = b; b = c;} return a;};
inline ll LCM(ll a, ll b) {return (a / GCD(a,b)) * b;};

priority_queue< ll, vector<ll>, greater<ll> > heap;

ld phi(int n) {
    int res = n;
    int m = n;
    FORE(i, 2, m) {
        if (m % i == 0) {
            res = res - res/i;
            while (m % i == 0)
                m /= i;
        }
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie();
    // freopen("/Users/macbook/Desktop/MyCPPLibrary/input", "r", stdin);
    // freopen("/Users/macbook/Desktop/MyCPPLibrary/output", "w", stdout);
    int nMax = 1e6 + 1;
    ld maxx = 0;
    int res = 2*3*5*7*11*13*17;
    cout << phi(510510) << endl;
    // FOR(i, 1, nMax) {
    //     ld phin = phi(i);
    //     if ((ld)i / phin > maxx) {
    //         maxx = (ld)i / phin;
    //         res = i;
    //     }
    //     cout << i << " " << phin << endl;
    // }
    cout << res << endl;
    return 0;
}
