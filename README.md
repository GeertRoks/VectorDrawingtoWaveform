# Vector Drawing to Waveform

### Roadmap

##### Step 1:

- [x]  Linear Bézier curves
- [x]  Straight line from (-1,-1) to (1,1) → saw wave or triangle wave
- [x]  read only one way or back and forth
- [x]  read the steps at different frequencies (step size through the line
- [x]  `def linearBezierOscillator(f, fs, duration, readDirection)`
    - [x]  `def linearBezier(p0, p1, t)` p0 and p1 complex, 0\<t\<1

##### Step 2:

- [ ]  Multiple linear Bézier curves chained together
- [ ]  Simple geometric shapes, such as rectangle and triangle
- [ ]  `def multiLinearBezierOscillator(f, fs, duration, readDirection)`
    - [ ]  go through multiple bezier curves that are connected with still a 0\<t\<1

##### Step 3:

- [ ]  Quadratic Bézier curve
- [ ]  Unit circle around origin → sine (build from 2 or 4 quadratic Bézier Curves)
- [ ]  `def multiQuadraticBezierOscillator(f, fs, duration, readDirection)`
    - [ ]  `def quadraticBezier(p0, p1, p2, t)` p0, p1 and p2 are complex, 0\<t\<1

##### Step 4: v 0.1.0

- [ ]  Complex drawing
- [ ]  playable on Keyboard (keys on computer)
- [ ]  Drawing sheet in web environment? (python + JS + HTML/CSS)
- [ ]  `simpleBezierOscillator(f, fs, path, readDirection)` path is an array of arrays. Each subarray is a bezier curve with 2 or 3 points.

--------------------------------
##### Future steps that aren't planned out yet

- [ ]  Cubic Bézier curve
- [ ]  C++ class
- [ ]  Read SVG file ([https://stackoverflow.com/questions/15857818/python-svg-parser](https://stackoverflow.com/questions/15857818/python-svg-parser))
- [ ]  Load SVG data into coordinate system centered around origin
- [ ]  Image edges to points
- [ ]  Approximate points with Bezier curves: [https://stackoverflow.com/questions/12643079/bézier-curve-fitting-with-scipy](https://stackoverflow.com/questions/12643079/b%C3%A9zier-curve-fitting-with-scipy)
