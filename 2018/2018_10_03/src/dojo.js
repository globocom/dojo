export const main = (p, m) => {
  let ret = []
  ret[0] = [0, 0]
  if (m > p) {
    for (let i = 1; i <= p; i++) {
      ret[i] = [i, i]
    }
  } else {
    let valor = m - 2
    let valor2 = (p - 1) / (m - 2)
    for (let i = 1; i <= valor; i++) {
      ret[i] = [(i - 1) * valor2 + 1, i * valor2]
    }
    ret.push([p, p])
  }
  return ret
}
