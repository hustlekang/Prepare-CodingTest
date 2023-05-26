const solution = (x, y, n) => {
    const dp = new Array(1_000_001).fill(Infinity);
    dp[x] = 0;

    for (let i = x; i < y + 1; i++){
        const a = i - n;
        const b = Number.isInteger(i / 2) ? i / 2 : -1;
        const c = Number.isInteger(i / 3) ? i / 3 : -1;

        [a,b,c].forEach(j => {
            if (j !== -1 && x <= j && dp[j] !== Infinity){
                dp[i] = Math.min(dp[i], dp[j] + 1);
            }
        })
    }
    const answer = dp[y] !== Infinity ? dp[y] : -1;

    return answer;
}