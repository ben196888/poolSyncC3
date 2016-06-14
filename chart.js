var chart = c3.generate({
  bindto: '#chart',
  data: {
    x: 'x',
    columns: [
      ['x', 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
      ['real', 78.23, 50.13, 44.18, 39.43, 36.54, 44.28, 37.82, 39.86, 46.07, 40.14],
      ['user', 8.72, 8.05, 7.74, 7.29, 7.00, 7.13, 6.90, 7.08, 7.20, 7.20],
      ['sys', 3.44, 3.50, 3.57, 3.56, 3.46, 3.54, 3.47, 3.55, 3.53, 3.67]
    ],
    axes: {
      user: 'y2',
      sys: 'y2'
    }
  },
  axis: {
    y2: {
      show: true
    }
  }
});

var plotChart = c3.generate({
  bindto: '#plotChart',
  data: {
    xs: {
      data10: 'data10_x',
      data20: 'data20_x',
      data30: 'data30_x',
      data40: 'data40_x',
      data50: 'data50_x',
      data60: 'data60_x',
      data70: 'data70_x',
      data80: 'data80_x',
      data90: 'data90_x',
      data100: 'data100_x'
    },
    url: 'data/all.csv'
  },
  type: 'scatter'
});