const solution = (players, callings) => {
    const mapByName = new Map();
    const mapByLocation = new Map();

    players.forEach((name,idx) => {
        mapByName.set(name,idx);
        mapByLocation.set(idx,name);
    })

    callings.forEach((name,i) => {
        const idx = mapByName.get(name); // 현재 위치
        const catchedName = mapByLocation.get(idx - 1); // 잡힌사람

        mapByName.set(name, idx - 1);
        mapByName.set(catchedName, idx);
        mapByLocation.set(idx,catchedName);
        mapByLocation.set(idx - 1, name);
    })

    return [...mapByLocation.values()];
}