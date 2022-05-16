# Number System Converter
<ul>
  <li>Script allows user to convert numeric values between different systems.</li>
  <li>Available systems are from base-2 to base-36.</li>
</ul>

# Requirements
<ul>
  <li>Script has been written in Python 3.9.4</li>
  <li>No additional libraries are needed</li>
</ul>

# Installation
<ul>
  <li>Nothing other than download and run</li>
</ul>

# Functions
<ul>
  <li>
    <b>SystemToDecimal(number, system)</b> - returns decimal number as an integer which was converted from given number in given system
    <br>
    <ul>
      <li>number - string containing number in given system</li>
      <li>system - system to be converted from</li>
    </ul>
    <br>
    <pre>1 print(SystemToDecimal('ZZA12C', 36)) # converts 'ZZA12C' from base-36 system<br>2 2175570660 # output is converted decimal number</pre>
  </li>
  
  <li>
    <b>DecimalToSystem(decimal, system)</b> - returns number as a string in given system from decimal number
    <br>
    <ul>
      <li>decimal - integer decimal number</li>
      <li>system - system to be converted to</li>
    </ul>
    <br>
    <pre>1 print(SystemToDecimal('ZZA12C', 36)) # converts 'ZZA12C' from base-36 system to decimal<br>2 2175570660 # output is decimal number</pre>
  </li>
  
  <li>
    <b>SystemToSystem(number, systemFrom, systemTo)</b> - returns number as a string in base-'systemTo' system converted from base-'systemFrom'
    <br>
    <ul>
      <li>number - string containing number in base-'systemFrom'</li>
      <li>systemFrom - system to be converted from</li>
      <li>systemTo - system to be converted to</li>
    </ul>
    <br>
    <pre>1 print(SystemToSystem('7126B3', 12, 6)) # converts '7126B3' from base-12 system to base-6<br>2 101512343 # output is converted base-6 number</pre>
  </li>
</ul>