const solution = (s, skip, index) => {
    const charArray = s.split('');
    const skipSet = new Set(skip);
    const answer = charArray
        .map(each => {
            let cnt = 0;
            let code = each.charCodeAt();

            while (cnt < index){
                code++;
                if (code === 'z'.charCodeAt() + 1) code = 'a'.charCodeAt();
                if (skipSet.has(String.fromCharCode(code))) continue;
                cnt++;
            }
            return String.fromCharCode(code);
        })
        .join('');
    
    return answer
}