const solution = (name, yearning, photo) => {
    const scoreByName = new Map();
    for (let i = 0; i < name.length; i++){
        scoreByName.set(name[i], yearning[i]);
    }

    const answer = photo.map(each =>
        each.reduce((acc, cur) => acc + (scoreByName.get(cur) ?? 0), 0));
    return answer;
}