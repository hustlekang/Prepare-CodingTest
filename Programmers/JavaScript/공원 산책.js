const solution = (park, routes) => {
  let location = [-1, -1];
  const H = park.length;
  const W = park[0].length;
  const dxdy = {
    N: [-1, 0],
    S: [1, 0],
    W: [0, -1],
    E: [0, 1],
  };

  for (let i = 0; i < H; i++) {
    if (location[0] !== -1) break;

    for (let j = 0; j < W; j++) {
      if (park[i][j] === "S") {
        location = [i, j];
        break;
      }
    }
  }

  for (const route of routes) {
    const [direction, cnt] = route.split(" ");
    const [dx, dy] = dxdy[direction];

    const movedX = location[0] + dx * cnt;
    const movedY = location[1] + dy * cnt;

    if (movedX < 0 || H <= movedX || movedY < 0 || W <= movedY) continue;

    let canGo = true;
    let [x, y] = [...location];
    for (let _ = 0; _ < cnt; _++) {
      x += dx;
      y += dy;
      if (park[x][y] === "X") {
        canGo = false;
        break;
      }
    }
    if (!canGo) continue;
    location = [movedX, movedY];
  }
  return location;
};
