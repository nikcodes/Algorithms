#include <iostream>
#include <bits/stdc++.h>
#include<cstdio>
#define ll long long int
#define mod 1000000007
#define pi 3.141592653589793
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front
#define vfind(a, e) find(a.begin(), a.end(), e)
#define forr(i, n) for (ll i = 0; i < n; i++)
#define rfor(i, n) for (ll i = n - 1; i >= 0; i--)
#define fors(i, b, e, steps) for(ll i = b; i < e; i += steps)
#define rfors(i, e, b, steps) for(ll i = e; i > b; i -= steps)
#define mp make_pair
using namespace std;

void gcd(ll a, ll b, ll &x, ll &y){
    if (a == 0){
        x = 0;
        y = 1;
        return;
    }


    gcd(b % a, a, x, y);
    ll yt = x;
    ll xt = y - (b / a) * x;
    x = xt;
    y = yt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cout << setprecision(10);
    
    
    ll a, b;
    cin >> a >> b;
    ll x, y;
    gcd(a, b, x, y);
    cout << x << ' ' << y;

}
