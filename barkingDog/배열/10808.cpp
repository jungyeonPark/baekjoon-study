// BOJ 10808번 알파벳 개수
#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    int arr[26];
    fill(arr, arr + 26, 0);
    for (auto c : s)
        arr[c - 'a']++;
    for (auto n : arr)
        cout << n << ' ';
}