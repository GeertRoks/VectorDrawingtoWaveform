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

- [x]  Multiple linear Bézier curves chained together
- [x]  Simple geometric shapes, such as rectangle and triangle
- [x]  `def multiLinearBezierOscillator(points, f, fs, duration, readDirection)`
    - [x]  go through multiple bezier curves that are connected with still a 0\<t\<1

##### Step 3:

- [x]  Quadratic Bézier curve
- [ ]  Unit circle around origin → sine (build from 2 or 4 quadratic Bézier Curves)
- [ ]  `def multiQuadraticBezierOscillator(points, f, fs, duration, readDirection)`
    - [x]  `def quadraticBezier(p0, p1, p2, t)` p0, p1 and p2 are complex, 0\<t\<1
    - [ ]  multiple quadratic bezier curves chained together

##### Step 4: v 0.1.0

- [ ]  Complex drawing
- [ ]  playable on Keyboard (keys on computer)
- [ ]  Drawing sheet in web environment? (python + JS + HTML/CSS)
- [ ]  `simpleBezierOscillator(path, f, fs, readDirection)`
    - path is an array of arrays. Each subarray is a bezier curve with 2 or 3 points.
    - f is a float that sets the frequency of the oscillator
    - fs is an int that sets the sample rate of the oscillator
    - readDirection is a string that sets the way the points are read (forward, backward or backforth)

--------------------------------
##### Future steps that aren't planned out yet

- [ ]  Cubic Bézier curve
- [ ]  C++ class
- [ ]  Read SVG file ([https://stackoverflow.com/questions/15857818/python-svg-parser](https://stackoverflow.com/questions/15857818/python-svg-parser))
- [ ]  Load SVG data into coordinate system centered around origin
- [ ]  Image edges to points
- [ ]  Approximate points with Bezier curves: [https://stackoverflow.com/questions/12643079/bézier-curve-fitting-with-scipy](https://stackoverflow.com/questions/12643079/b%C3%A9zier-curve-fitting-with-scipy)
