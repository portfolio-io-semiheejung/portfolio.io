from bs4 import BeautifulSoup
import pandas as pd

html="""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div class="results group-everything">
<div class="totals total-all text-right">269 results</div>
<a class="result" href="/mongoose">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1231/0TXzZU7W_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mongoose</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">170</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Let's face it, writing MongoDB validation, casting and business logic boilerplate is a drag. That's why we wrote Mongoose. Mongoose provides a straight-forward, schema-based solution to modeling your application data and includes built-in type casting, validation, query building, business logic hooks and more, out of the box.</span>
  </a><a class="result" href="/javascript">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1209/javascript.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">JavaScript</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12867</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">JavaScript is most known as the scripting language for Web pages, but used in many non-browser environments as well such as node.js or Apache CouchDB. It is a prototype-based, multi-paradigm scripting language that is dynamic,and supports object-oriented, imperative, and functional programming styles. </span>
  </a><a class="result" href="/jquery">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1021/lxEKmMnB_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">jQuery</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">106409</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">jQuery is a cross-platform JavaScript library designed to simplify the client-side scripting of HTML.</span>
  </a><a class="result" href="/python">"
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/993/pUBY5pVj.png>
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Python</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7288</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Python is a general purpose programming language created by Guido Van Rossum. Python is most praised for its elegant syntax and readable code, if you are just beginning your programming career python suits you best.</span>
  </a><a class="result" href="/nodejs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1011/n1JRsFeB_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Node.js</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7572</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient, perfect for data-intensive real-time applications that run across distributed devices.</span>
  </a><a class="result" href="/php">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/991/hwUcGZ41_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PHP</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">43889</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Fast, flexible and pragmatic, PHP powers everything from your blog to the most popular websites in the world.</span>
  </a><a class="result" href="/react">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1020/OYIaJ1KK.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">React</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">9228</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Lots of people use React as the V in MVC. Since React makes no assumptions about the rest of your technology stack, it's easy to try it out on a small feature in an existing project.</span>
  </a><a class="result" href="/nginx">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1052/YMxUfyWf.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">nginx</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">41868</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">nginx [engine x] is an HTTP and reverse proxy server, as well as a mail proxy server, written by Igor Sysoev. According to Netcraft nginx served or proxied 30.46% of the top million busiest sites in Jan 2018.</span>
  </a><a class="result" href="/java">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/995/K85ZWV2F.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Java</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">9706</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Java is a programming language and computing platform first released by Sun Microsystems in 1995. There are lots of applications and websites that will not work unless you have Java installed, and more are created every day. Java is fast, secure, and reliable. From laptops to datacenters, game consoles to scientific supercomputers, cell phones to the Internet, Java is everywhere!</span>
  </a><a class="result" href="/html5">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2538/kEpgHiC9.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">HTML5</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5077</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">HTML5 is a core technology markup language of the Internet used for structuring and presenting content for the World Wide Web. As of October 2014 this is the final and complete fifth revision of the HTML standard of the World Wide Web Consortium (W3C). The previous version, HTML 4, was standardised in 1997.</span>
  </a><a class="result" href="/mysql">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1025/logo-mysql-170x170.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">MySQL</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4835</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The MySQL software delivers a very fast, multi-threaded, multi-user, and robust SQL (Structured Query Language) database server. MySQL Server is intended for mission-critical, heavy-load production systems as well as for embedding into mass-deployed software.</span>
  </a><a class="result" href="/google-fonts">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2652/ZWREQYdH_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Fonts</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">60445</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A library of 915 free licensed fonts, an interactive web directory for browsing the library, and APIs for conveniently using the fonts via CSS and Android.</span>
  </a><a class="result" href="/mongodb">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1030/leaf-360x360.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">MongoDB</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3520</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">MongoDB stores data in JSON-like documents that can vary in structure, offering a dynamic, flexible schema. MongoDB was also designed for high availability and scalability, with built-in replication and auto-sharding.</span>
  </a><a class="result" href="/postgresql">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1028/ASOhU5xJ.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PostgreSQL</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4618</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, user-defined types
and functions.</span>
  </a><a class="result" href="/apache-httpd">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1051/fab.os.logo.apache.200.15011_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache HTTP Server</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">37502</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The Apache HTTP Server is a powerful and flexible HTTP/1.1 compliant web server.  Originally designed as a replacement for the NCSA HTTP Server, it has grown to be the most popular web server on the Internet.</span>
  </a><a class="result" href="/bootstrap">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1101/C9QJ7V3X.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bootstrap</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">43012</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Bootstrap is the most popular HTML, CSS, and JS framework for developing responsive, mobile first projects on the web.</span>
  </a><a class="result" href="/ubuntu">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3511/cof_orange_hex.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Ubuntu</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">10075</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Ubuntu is an ancient African word meaning ‘humanity to others’. It also means ‘I am what I am because of who we all are’. The Ubuntu operating system brings the spirit of Ubuntu to the world of computers.</span>
  </a><a class="result" href="/angularjs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1019/square.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AngularJS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6794</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AngularJS lets you write client-side web applications as if you had a smarter browser. It lets you use good old HTML (or HAML, Jade and friends!) as your template language and lets you extend HTML’s syntax to express your application’s components clearly and succinctly. It automatically synchronizes data from your UI (view) with your JavaScript objects (model) through 2-way data binding.</span>
  </a><a class="result" href="/redis">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1031/redis.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Redis</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5141</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Redis is an open source, BSD licensed, advanced key-value store. It is often referred to as a data structure server since keys can contain strings, hashes, lists, sets and sorted sets.</span>
  </a><a class="result" href="/amazon-ec2">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/18/amazon-ec2.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon EC2</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6244</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a web service that provides resizable compute capacity in the cloud. It is designed to make web-scale computing easier for developers.</span>
  </a><a class="result" href="/amazon-s3">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/25/amazon-s3.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon S3</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5913</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon Simple Storage Service provides a fully redundant data storage infrastructure for storing and retrieving any amount of data, at any time, from anywhere on the web</span>
  </a><a class="result" href="/es6">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4109/16407404782_8b9c57eab3.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ES6</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2441</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Goals for ECMAScript 2015 include providing better support for large applications, library creation, and for use of ECMAScript as a compilation target for other languages. Some of its major enhancements include modules, class declarations, lexical block scoping, iterators and generators, promises for asynchronous programming, destructuring patterns, and proper tail calls.</span>
  </a><a class="result" href="/typescript">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1612/bynNY5dJ.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">TypeScript</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3172</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">TypeScript is a language for application-scale JavaScript development. It's a typed superset of JavaScript that compiles to plain JavaScript.</span>
  </a><a class="result" href="/jquery-ui">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1022/jqueryui_avatar_96.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">jQuery UI</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">24245</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Whether you're building highly interactive web applications or you just need to add a date picker to a form control, jQuery UI is the perfect choice.</span>
  </a><a class="result" href="/vue-js">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3837/paeckCWC.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Vue.js</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2828</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a library for building interactive web interfaces. It provides data-reactive components with a simple and flexible API. </span>
  </a><a class="result" href="/c-sharp">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1015/1200px-C_Sharp_wordmark.svg.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">C#</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2094</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">C# (pronounced "See Sharp") is a simple, modern, object-oriented, and type-safe programming language. C# has its roots in the C family of languages and will be immediately familiar to C, C++, Java, and JavaScript programmers.</span>
  </a><a class="result" href="/sass">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1171/jCR2zNJV.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sass</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3216</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Sass is an extension of CSS3, adding nested rules, variables, mixins, selector inheritance, and more. It's translated to well-formatted, standard CSS using the command line tool or a web-framework plugin.</span>
  </a><a class="result" href="/ruby">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/989/ruby.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Ruby</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5598</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Ruby is a language of careful balance. Its creator, Yukihiro “Matz” Matsumoto, blended parts of his favorite languages (Perl, Smalltalk, Eiffel, Ada, and Lisp) to form a new language that balanced functional programming with imperative programming.</span>
  </a><a class="result" href="/firebase">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/116/cZLxNFZS.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Firebase</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2070</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Firebase is a cloud service designed to power real-time, collaborative applications. Simply add the Firebase library to your application to gain access to a shared data structure; any changes you make to that data are automatically synchronized with the Firebase cloud and with other clients within milliseconds.</span>
  </a><a class="result" href="/django">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/994/4aGjtNQv.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Django</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2141</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.</span>
  </a><a class="result" href="/heroku">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/133/3wgIDj3j.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Heroku</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2135</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Heroku is a cloud application platform – a new way of building and deploying web apps. Heroku lets app developers spend 100% of their time on their application code, not managing servers, deployment, ongoing operations, or scaling.</span>
  </a><a class="result" href="/react-native">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2699/KoK6gHzp.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">React Native</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1361</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">React Native enables you to build world-class application experiences on native platforms using a consistent developer experience based on JavaScript and React. The focus of React Native is on developer efficiency across all the platforms you care about - learn once, write anywhere. Facebook uses React Native in multiple production apps and will continue investing in React Native.</span>
  </a><a class="result" href="/laravel">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/992/AcA2LnWL_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Laravel</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2954</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a web application framework with expressive, elegant syntax. It attempts to take the pain out of development by easing common tasks used in the majority of web projects, such as authentication, routing, sessions, and caching.</span>
  </a><a class="result" href="/android">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1010/m8jf0po4imu8t5eemjdd.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Android SDK</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1750</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Android provides a rich application framework that allows you to build innovative apps and games for mobile devices in a Java language environment.</span>
  </a><a class="result" href="/reduxjs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4074/13142323.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Redux</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1848</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It helps you write applications that behave consistently, run in different environments (client, server, and native), and are easy to test. t provides a great experience, such as live code editing combined with a time traveling debugger.</span>
  </a><a class="result" href="/expressjs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1163/hashtag.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ExpressJS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1610</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Express is a minimal and flexible node.js web application framework, providing a robust set of features for building single and multi-page, and hybrid web applications.</span>
  </a><a class="result" href="/graphql">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3820/12972006.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GraphQL</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1254</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">GraphQL is a data query language and runtime designed and used at Facebook to request and deliver data to mobile and web apps since 2012.</span>
  </a><a class="result" href="/rails">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/990/x57_Lorv.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Rails</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3440</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Rails is a web-application framework that includes everything needed to create database-backed web applications according to the Model-View-Controller (MVC) pattern.</span>
  </a><a class="result" href="/css-3">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6727/css.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">CSS 3</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2762</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">CSS3 is the latest evolution of the Cascading Style Sheets language and aims at extending CSS2.1. It brings a lot of long-awaited novelties, like rounded corners, shadows, gradients, transitions or animations, as well as new layouts like multi-columns, flexible box or grid layouts. Experimental parts are vendor-prefixed and should either be avoided in production environments, or used with extreme caution as both their syntax and semantics can change in the future.</span>
  </a><a class="result" href="/asp-net">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6755/2c45151a4a11d3a3c8e71bb34dd069d6_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ASP.NET</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12641</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">.NET is a developer platform made up of tools, programming languages, and libraries for building many different types of applications.</span>
  </a><a class="result" href="/digitalocean">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/295/Onjxs6Lw_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">DigitalOcean</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2490</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">We take the complexities out of cloud hosting by offering blazing fast, on-demand SSD cloud servers, straightforward pricing, a simple API, and an easy-to-use control panel. </span>
  </a><a class="result" href="/spring-boot">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2927/nPzvMuo2_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Spring Boot</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">697</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications that you can "just run". We take an opinionated view of the Spring platform and third-party libraries so you can get started with minimum fuss. Most Spring Boot applications need very little Spring configuration.</span>
  </a><a class="result" href="/microsoft-azure">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/213/W9gT7hZo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Microsoft Azure</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4321</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Azure is an open and flexible cloud platform that enables you to quickly build, deploy and manage applications across a global network of Microsoft-managed datacenters. You can build applications using any language, tool or framework. And you can integrate your public cloud applications with your existing IT environment.</span>
  </a><a class="result" href="/aws-lambda">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1909/aws-lambda.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS Lambda</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1850</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AWS Lambda is a compute service that runs your code in response to events and automatically manages the underlying compute resources for you. You can use AWS Lambda to extend other AWS services with custom logic, or create your own back-end services that operate at AWS scale, performance, and security.</span>
  </a><a class="result" href="/go">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1005/O6AczwfV_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Go</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2325</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.</span>
  </a><a class="result" href="/kafka">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1063/kazUJooF_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Kafka</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">938</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Kafka is a distributed, partitioned, replicated commit log service. It provides the functionality of a messaging system, but with a unique design.</span>
  </a><a class="result" href="/rabbitmq">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1061/rabbit.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">RabbitMQ</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1486</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">RabbitMQ gives your applications a common platform to send and receive messages, and your messages a safe place to live until received.</span>
  </a><a class="result" href="/flask">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1001/flask.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Flask</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">880</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Flask is intended for getting started very quickly and was developed with best intentions in mind.</span>
  </a><a class="result" href="/markdown">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1147/markdown.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Markdown</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1189</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Markdown is two things: (1) a plain text formatting syntax; and (2) a software tool, written in Perl, that converts the plain text formatting to HTML. </span>
  </a><a class="result" href="/swift">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1009/tuHsaI2U.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Swift</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2004</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Writing code is interactive and fun, the syntax is concise yet expressive, and apps run lightning-fast. Swift is ready for your next iOS and OS X project — or for addition into your current app — because Swift code works side-by-side with Objective-C.</span>
  </a><a class="result" href="/tomcat">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1187/tomcat.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache Tomcat</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1684</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Apache Tomcat powers numerous large-scale, mission-critical web applications across a diverse range of industries and organizations.</span>
  </a><a class="result" href="/microsoft-iis">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1056/J5gFiHbG.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Microsoft IIS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5825</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Internet Information Services (IIS) for Windows Server is a flexible, secure and manageable Web server for hosting anything on the Web. From media streaming to web applications, IIS's scalable and open architecture is ready to handle the most demanding tasks.</span>
  </a><a class="result" href="/amazon-rds-for-mysql">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/232/amazon-rds.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon RDS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2237</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon RDS gives you access to the capabilities of a familiar MySQL, Oracle or Microsoft SQL Server database engine. This means that the code, applications, and tools you already use today with your existing databases can be used with Amazon RDS. Amazon RDS automatically patches the database software and backs up your database, storing the backups for a user-defined retention period and enabling point-in-time recovery. You benefit from the flexibility of being able to scale the compute resources or storage capacity associated with your Database Instance (DB Instance) via a single API call.</span>
  </a><a class="result" href="/microsoft-sql-server">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1027/sql_server.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Microsoft SQL Server</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">857</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Microsoft® SQL Server is a database management and analysis system for e-commerce, line-of-business, and data warehousing solutions. </span>
  </a><a class="result" href="/sqlite">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1071/sqlite.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">SQLite</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">595</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">SQLite is an embedded SQL database engine. Unlike most other SQL databases, SQLite does not have a separate server process. SQLite reads and writes directly to ordinary disk files. A complete SQL database with multiple tables, indices, triggers, and views, is contained in a single disk file.</span>
  </a><a class="result" href="/google-cloud-platform">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4240/1a61e4pu_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Cloud Platform</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7846</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It helps you build what's next with secure infrastructure, developer tools, APIs, data analytics and machine learning. It is a suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products, such as Google Search and YouTube.</span>
  </a><a class="result" href="/mariadb">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1615/mariadb-logo-400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">MariaDB</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">851</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Started by core members of the original MySQL team, MariaDB actively works with outside developers to deliver the most featureful, stable, and sanely licensed open SQL server in the industry. MariaDB is designed as a drop-in replacement of MySQL(R) with more features, new storage engines, fewer bugs, and better performance.
</span>
  </a><a class="result" href="/debian">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1656/vd4gAekh.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Debian</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1886</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Debian systems currently use the Linux kernel or the FreeBSD kernel. Linux is a piece of software started by Linus Torvalds and supported by thousands of programmers worldwide. FreeBSD is an operating system including a kernel and other software.</span>
  </a><a class="result" href="/centos">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3069/centos-icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">CentOS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2483</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The CentOS Project is a community-driven free software effort focused on delivering a robust open source ecosystem. For users, we offer a consistent manageable platform that suits a wide variety of deployments. For open source communities, we offer a solid, predictable base to build upon, along with extensive resources to build, test, release, and maintain their code.</span>
  </a><a class="result" href="/google-compute-engine">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/518/s01TMTGn.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Compute Engine</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">993</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Google Compute Engine is a service that provides virtual machines that run on Google infrastructure. Google Compute Engine offers scale, performance, and value that allows you to easily launch large compute clusters on Google's infrastructure. There are no upfront investments and you can run up to thousands of virtual CPUs on a system that has been designed from the ground up to be fast, and to offer strong consistency of performance.</span>
  </a><a class="result" href="/amazon-ec2-container-service">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1908/amazon-ecs.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon EC2 Container Service</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1259</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon EC2 Container Service lets you launch and stop container-enabled applications with simple API calls, allows you to query the state of your cluster from a centralized service, and gives you access to many familiar Amazon EC2 features like security groups, EBS volumes and IAM roles.</span>
  </a><a class="result" href="/socket-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1161/vI0ZZlhZ_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Socket.IO</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1209</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It enables real-time bidirectional event-based communication. It works on every platform, browser or device, focusing equally on reliability and speed.</span>
  </a><a class="result" href="/cplusplus">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1049/cplusplus.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">C++</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1287</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">C++ compiles directly to a machine's native code, allowing it to be one of the fastest languages in the world, if optimized.</span>
  </a><a class="result" href="/material-design-for-angular">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1523/square.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Material Design for Angular</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">472</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Material Design is a specification for a unified system of visual, motion, and interaction design that adapts across different devices. Our goal is to deliver a lean, lightweight set of AngularJS-native UI elements that implement the material design system for use in Angular SPAs.</span>
  </a><a class="result" href="/objective-c">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1008/xcode.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Objective-C</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2168</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Objective-C is a superset of the C programming language and provides object-oriented capabilities and a dynamic runtime. Objective-C inherits the syntax, primitive types, and flow control statements of C and adds syntax for defining classes and methods. It also adds language-level support for object graph management and object literals while providing dynamic typing and binding, deferring many responsibilities until runtime.</span>
  </a><a class="result" href="/ionic">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/876/bYMCvtHD_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Ionic</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">641</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Free and open source, Ionic offers a library of mobile and desktop-optimized HTML, CSS and JS components for building highly interactive apps. Use with Angular, React, Vue, or plain JavaScript.</span>
  </a><a class="result" href="/google-app-engine">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/139/s01TMTGn.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google App Engine</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">908</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Google has a reputation for highly reliable, high performance infrastructure. With App Engine you can take advantage of the 10 years of knowledge Google has in running massively scalable, performance driven systems. App Engine applications are easy to build, easy to maintain, and easy to scale as your traffic and data storage needs grow. </span>
  </a><a class="result" href="/scala">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1012/scala.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Scala</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">889</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Scala is an acronym for “Scalable Language”. This means that Scala grows with you. You can play with it by typing one-line expressions and observing the results. But you can also rely on it for large mission critical systems, as many companies, including Twitter, LinkedIn, or Intel do. To some, Scala feels like a scripting language. Its syntax is concise and low ceremony; its types get out of the way because the compiler can infer them. </span>
  </a><a class="result" href="/electron">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2946/XJRdVxx3.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Electron</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">394</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With Electron, creating a desktop application for your company or idea is easy. Initially developed for GitHub's Atom editor, Electron has since been used to create applications by companies like Microsoft, Facebook, Slack, and Docker. The Electron framework lets you write cross-platform desktop applications using JavaScript, HTML and CSS. It is based on io.js and Chromium and is used in the Atom editor.</span>
  </a><a class="result" href="/animate-css">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9195/animate-css.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Animate.css </span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7374</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a bunch of cool, fun, and cross-browser animations for you to use in your projects. Great for emphasis, home pages, sliders, and general just-add-water-awesomeness.</span>
  </a><a class="result" href="/dot-net">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1014/IoPy1dce_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">.NET</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2067</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">.NET is a general purpose development platform. With .NET, you can use multiple languages, editors, and libraries to build native applications for web, mobile, desktop, gaming, and IoT for Windows, macOS, Linux, Android, and more.</span>
  </a><a class="result" href="/openssl">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3091/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OpenSSL</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4146</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a robust, commercial-grade, and full-featured toolkit for the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols. It is also a general-purpose cryptography library.</span>
  </a><a class="result" href="/slick">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1843/slick.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Slick</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7801</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a modern database query and access library for Scala. It allows you to work with stored data almost as if you were using Scala collections while at the same time giving you full control over when a database access happens and which data is transferred. </span>
  </a><a class="result" href="/backbone">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1017/Screen_Shot_2012-04-28_at_8.52.15_PM.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Backbone.js</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3424</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Backbone supplies structure to JavaScript-heavy applications by providing models key-value binding and custom events, collections with a rich API of enumerable functions, views with declarative event handling, and connects it all to your existing application over a RESTful JSON interface.</span>
  </a><a class="result" href="/memcached">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1040/memcached-logo-200x152.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Memcached</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1029</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Memcached is an in-memory key-value store for small chunks of arbitrary data (strings, objects) from results of database calls, API calls, or page rendering.</span>
  </a><a class="result" href="/symfony">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1197/logosf_positif_03_icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Symfony</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">655</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is written with speed and flexibility in mind. It allows developers to build better and easy to maintain websites with PHP..</span>
  </a><a class="result" href="/c">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/no-img-open-source.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">C</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1170</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional"></span>
  </a><a class="result" href="/angular-2">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3745/cb8U-gL6_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Angular 2</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">694</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a TypeScript-based open-source web application framework. It is a development platform for building mobile and desktop web applications.</span>
  </a><a class="result" href="/handlebars">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1143/Handlebars.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Handlebars.js</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3159</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Handlebars.js is an extension to the Mustache templating language created by Chris Wanstrath. Handlebars.js and Mustache are both logicless templating languages that keep the view and the code separated like we all know they should be.</span>
  </a><a class="result" href="/addthis">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3421/T3VyOpzk_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AddThis</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5787</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It provide tools that make it easier to share content across the social web, and provides publishers with increased traffic and in-depth analytics.</span>
  </a><a class="result" href="/kotlin">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3750/pCfEzr6L.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Kotlin</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">815</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Kotlin is a statically typed programming language for the JVM, Android and the browser, 100% interoperable with Java</span>
  </a><a class="result" href="/cassandra">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1032/cassandra_small.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Cassandra</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">484</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Partitioning means that Cassandra can distribute your data across multiple machines in an application-transparent matter. Cassandra will automatically repartition as machines are added and removed from the cluster. Row store means that like relational databases, Cassandra organizes data by rows and columns. The Cassandra Query Language (CQL) is a close relative of SQL.</span>
  </a><a class="result" href="/spring">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/996/unnamed.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Spring</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">493</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A key element of Spring is infrastructural support at the application level: Spring focuses on the "plumbing" of enterprise applications so that teams can focus on application-level business logic, without unnecessary ties to specific deployment environments.</span>
  </a><a class="result" href="/fancybox">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8986/ndGU91r2_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">fancybox</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5334</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a tool that offers a nice and elegant way to add zooming functionality for images, html content and multi-media on your webpages. It is built on the top of the popular JavaScript framework jQuery and is both easy to implement and a snap to customize.</span>
  </a><a class="result" href="/amazon-dynamodb">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/389/amazon-dynamodb.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon DynamoDB</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">739</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With it , you can offload the administrative burden of operating and scaling a highly available distributed database cluster, while paying a low price for only what you use.</span>
  </a><a class="result" href="/flutter">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7180/flutter-mark-square-100.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Flutter</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">141</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Flutter is a mobile app SDK to help developers and designers build modern mobile apps for iOS and Android.</span>
  </a><a class="result" href="/lodash">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2438/lodash.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Lodash</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3123</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A JavaScript utility library delivering consistency, modularity, performance, &amp; extras. It provides utility functions for common programming tasks using the functional programming paradigm.</span>
  </a><a class="result" href="/elixir">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1974/drop.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Elixir</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">419</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Elixir leverages the Erlang VM, known for running low-latency, distributed and fault-tolerant systems, while also being successfully used in web development and the embedded software domain.</span>
  </a><a class="result" href="/typekit">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1913/New_Project__7_.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Typekit</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4046</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an online service which offers a subscription library of high-quality fonts. The fonts may be used directly on websites or synced via Adobe Creative Cloud to applications on the subscriber's computers.</span>
  </a><a class="result" href="/codeigniter">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1195/ci_logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">CodeIgniter</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1724</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">CodeIgniter is a proven, agile &amp; open PHP web application framework with a small footprint. It is powering the next generation of web apps.</span>
  </a><a class="result" href="/rust">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1070/v7txhrjp9pdqrkdtxxp0.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Rust</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">201</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Rust is a systems programming language that combines strong compile-time correctness guarantees with fast performance. It improves upon the ideas of other systems languages like C++ by providing guaranteed memory safety (no crashes, no data races) and complete control over the lifecycle of memory.</span>
  </a><a class="result" href="/coffeescript">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1178/slQydAMv.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">CoffeeScript</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1048</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It adds syntactic sugar inspired by Ruby, Python and Haskell in an effort to enhance JavaScript's brevity and readability. Specific additional features include list comprehension and de-structuring assignment.</span>
  </a><a class="result" href="/spark">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2220/ca72c4715da998b0bf5d1c857958bed3.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache Spark</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">419</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Spark is a fast and general processing engine compatible with Hadoop data. It can run in Hadoop clusters through YARN or Spark's standalone mode, and it can process data in HDFS, HBase, Cassandra, Hive, and any Hadoop InputFormat. It is designed to perform both batch processing (similar to MapReduce) and new workloads like streaming, interactive queries, and machine learning.</span>
  </a><a class="result" href="/moment-js">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3643/Xrtdc94q_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Moment.js</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3039</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A javascript date library for parsing, validating, manipulating, and formatting dates.</span>
  </a><a class="result" href="/meteor">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1162/uJPMDhZq.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Meteor</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">318</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A Meteor application is a mix of JavaScript that runs inside a client web browser, JavaScript that runs on the Meteor server inside a Node.js container, and all the supporting HTML fragments, CSS rules, and static assets. </span>
  </a><a class="result" href="/hadoop">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1044/elephant_rgb_sq.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Hadoop</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">354</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage.</span>
  </a><a class="result" href="/aws-elastic-beanstalk">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/210/aws-elastic-beanstalk.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS Elastic Beanstalk</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">550</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Once you upload your application, Elastic Beanstalk automatically handles the deployment details of capacity provisioning, load balancing, auto-scaling, and application health monitoring.</span>
  </a><a class="result" href="/gatsbyjs">
    <div style="display:inline-block">
      <img src="https://ucarecdn.com/04b55b4e-0ecc-4003-a89e-98f674075b3e/">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gatsby</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">411</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Gatsby lets you build blazing fast sites with your data, whatever the source. Liberate your sites from legacy CMSs and fly into the future.</span>
  </a><a class="result" href="/less">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1170/3538330.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Less</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">720</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Less is a CSS pre-processor, meaning that it extends the CSS language, adding features that allow variables, mixins, functions and many other techniques that allow you to make CSS that is more maintainable, themable and extendable.</span>
  </a><a class="result" href="/d3">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1491/HgKolWB5_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">D3.js</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">671</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a JavaScript library for manipulating documents based on data. Emphasises on web standards gives you the full capabilities of modern browsers without tying yourself to a proprietary framework.</span>
  </a><a class="result" href="/amazon-sqs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/395/amazon-sqs.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon SQS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">636</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Transmit any volume of data, at any level of throughput, without losing messages or requiring other services to be always available. With SQS, you can offload the administrative burden of operating and scaling a highly available messaging cluster, while paying a low price for only what you use.</span>
  </a><a class="result" href="/select2">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7488/select2.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Select2</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2747</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It gives you a customizable select box with support for searching, tagging, remote data sets, infinite scrolling, and many other highly used options. It comes with support for RTL environments, searching with diacritics and over 40 languages built-in.</span>
  </a><a class="result" href="/r-language">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1213/r-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">R Language</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">367</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">R provides a wide variety of statistical (linear and nonlinear modelling, classical statistical tests, time-series analysis, classification, clustering, ...) and graphical techniques, and is highly extensible.</span>
  </a><a class="result" href="/dart">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1646/Twitter-02.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Dart</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">89</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Dart is a cohesive, scalable platform for building apps that run on the web (where you can use Polymer) or on servers (such as with Google Cloud Platform). Use the Dart language, libraries, and tools to write anything from simple scripts to full-featured apps.</span>
  </a><a class="result" href="/apollo">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5508/CyUH653y.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apollo</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">344</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Build a universal GraphQL API on top of your existing REST APIs, so you can ship new application features fast without waiting on backend changes.</span>
  </a><a class="result" href="/underscore">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1150/underscore-js.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Underscore</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1168</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A JavaScript library that provides a whole mess of useful functional programming helpers without extending any built-in objects. </span>
  </a><a class="result" href="/material-ui">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1904/_.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Material-UI</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">135</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a comprehensive guide for visual, motion, and interaction design across platforms and devices.</span>
  </a><a class="result" href="/django-rest-framework">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1630/New_Project__67_.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Django REST framework</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">280</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a powerful and flexible toolkit that makes it easy to build Web APIs.</span>
  </a><a class="result" href="/next-js">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5936/nextjs.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Next.js</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">507</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Next.js is a minimalistic framework for server-rendered React applications.</span>
  </a><a class="result" href="/foundation">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1105/ocLJW3ku_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Foundation</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">748</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Foundation is the most advanced responsive front-end framework in the world. You can quickly prototype and build sites or apps that work on any kind of device with Foundation, which includes layout constructs (like a fully responsive grid), elements and best practices.</span>
  </a><a class="result" href="/dot-net-core">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6403/9141961.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">.NET Core</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">175</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Cross-platform (supporting Windows, macOS, and Linux) and can be used to build device, cloud, and IoT applications.</span>
  </a><a class="result" href="/celery">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1075/celery.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Celery</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">409</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Celery is an asynchronous task queue/job queue based on distributed message passing.	It is focused on real-time operation, but supports scheduling as well.</span>
  </a><a class="result" href="/openresty">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3118/openresty.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OpenResty</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2035</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">OpenResty (aka. ngx_openresty) is a full-fledged web application server by bundling the standard Nginx core, lots of 3rd-party Nginx modules, as well as most of their external dependencies.</span>
  </a><a class="result" href="/perl">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1048/perl.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Perl</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">814</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Perl is a general-purpose programming language originally developed for
text manipulation and now used for a wide range of tasks including
system administration, web development, network programming, GUI
development, and more.</span>
  </a><a class="result" href="/oracle">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1026/jT-HJYJg.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Oracle</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">203</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Oracle Database is an RDBMS. An RDBMS that implements object-oriented features such as user-defined types, inheritance, and polymorphism is called an object-relational database management system (ORDBMS). Oracle Database has extended the relational model to an object-relational model, making it possible to store complex business models in a relational database.</span>
  </a><a class="result" href="/prototype">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3597/o_bigger_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Prototype</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2110</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Prototype is a JavaScript framework that aims to ease development of dynamic web applications. It offers a familiar class-style OO framework, extensive Ajax support, higher-order programming constructs, and easy DOM manipulation.</span>
  </a><a class="result" href="/linux">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/10483/linux.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Linux</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">111</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A clone of the operating system Unix, written from scratch by Linus Torvalds with assistance from a loosely-knit team of hackers across the Net. It aims towards POSIX and Single UNIX Specification compliance.</span>
  </a><a class="result" href="/xamarin">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/211/RDXWoY7W.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Xamarin</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">128</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Xamarin’s Mono-based products enable .NET developers to use their existing code, libraries and tools (including Visual Studio*), as well as skills in .NET and the C# programming language, to create mobile applications for the industry’s most widely-used mobile devices, including Android-based smartphones and tablets, iPhone, iPad and iPod Touch.</span>
  </a><a class="result" href="/react-router">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3350/8261421.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">React Router</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">346</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">React Router is a complete routing solution designed specifically for React.js. It painlessly synchronizes the components of your application with the URL, with first-class support for nesting, transitions, and server side rendering.</span>
  </a><a class="result" href="/clojure">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1003/Clojure_300x300.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Clojure</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">239</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Clojure is designed to be a general-purpose language, combining the approachability and interactive development of a scripting language with an efficient and robust infrastructure for multithreaded programming. Clojure is a compiled language - it compiles directly to JVM bytecode, yet remains completely dynamic. Clojure is a dialect of Lisp, and shares with Lisp the code-as-data philosophy and a powerful macro system.</span>
  </a><a class="result" href="/pug">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1175/pug.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Pug</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">244</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">This project was formerly known as "Jade." Pug is a high performance template engine heavily influenced by Haml and implemented with JavaScript for Node.js and browsers.</span>
  </a><a class="result" href="/emberjs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1018/3s1seyc0csl75btyw1vl.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Ember.js</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">501</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A JavaScript framework that does all of the heavy lifting that you'd normally have to do by hand. There are tasks that are common to every web app; It does those things for you, so you can focus on building killer features and UI.</span>
  </a><a class="result" href="/amazon-vpc">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/388/amazon-vpc.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon VPC</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">451</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways. You can easily customize the network configuration for your Amazon VPC.</span>
  </a><a class="result" href="/semantic-ui">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1106/semantic-ui.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Semantic UI</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">122</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Semantic empowers designers and developers by creating a shared vocabulary for UI.</span>
  </a><a class="result" href="/quantcast">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4374/SiHaeog__400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Quantcast</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1924</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a digital marketing company that provides free audience demographics measurement and delivers real-time advertising.</span>
  </a><a class="result" href="/amazon-elasticache">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/392/amazon-elasticache.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon ElastiCache</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">512</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">ElastiCache improves the performance of web applications by allowing you to retrieve information from fast, managed, in-memory caches, instead of relying entirely on slower disk-based databases. ElastiCache supports Memcached and Redis.</span>
  </a><a class="result" href="/google-cloud-storage">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/694/Cloud_Storage.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Cloud Storage</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">321</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Google Cloud Storage allows world-wide storing and retrieval of any amount of data and at any time. It provides a simple programming interface which enables developers to take advantage of Google's own reliable and fast networking infrastructure to perform data operations in a secure and cost effective manner. If expansion needs arise, developers can benefit from the scalability provided by Google's infrastructure.</span>
  </a><a class="result" href="/gravity-forms">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9006/w8NDcWwU_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gravity Forms</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1858</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a WordPress plugin used originally for contact forms, but in a more general sense, it allows site owners to create forms to collect information. It can be used for contact forms, WordPress post creation, calculators, employment applications and more.</span>
  </a><a class="result" href="/red-hat-openshift">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/197/854d85d0c77271af224b455f81b5fc88.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Red Hat OpenShift</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">117</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">OpenShift is Red Hat's Cloud Computing Platform as a Service (PaaS) offering. OpenShift is an application platform in the cloud where application developers and teams can build, test, deploy, and run their applications.</span>
  </a><a class="result" href="/amazon-redshift">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/386/amazon-redshift.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon Redshift</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">384</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is optimized for data sets ranging from a few hundred gigabytes to a petabyte or more and costs less than $1,000 per terabyte per year, a tenth the cost of most traditional data warehousing solutions.</span>
  </a><a class="result" href="/litespeed">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2873/9lxca5AK_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">LiteSpeed</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1752</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a drop-in Apache replacement and the leading high-performance, high-scalability server. You can replace your existing Apache server with it without changing your configuration or operating system details. As a drop-in replacement, it allows you to quickly eliminate Apache bottlenecks in 15 minutes with zero downtime. </span>
  </a><a class="result" href="/yui">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3372/yui.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">YUI Library</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1795</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a free, open source JavaScript and CSS library for building richly interactive web applications. Its lightweight core and modular architecture make it scalable, fast, and robust. </span>
  </a><a class="result" href="/airflow">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3130/airflow.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Airflow</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">174</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Use Airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command lines utilities makes performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress and troubleshoot issues when needed.</span>
  </a><a class="result" href="/json">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2880/1024px-JSON_vector_logo.svg.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">JSON</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">85</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">JavaScript Object Notation is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language.</span>
  </a><a class="result" href="/mustache">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1142/197655.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mustache</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1289</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Mustache is a logic-less template syntax. It can be used for HTML, config files, source code - anything. It works by expanding tags in a template using values provided in a hash or object. We call it "logic-less" because there are no if statements, else clauses, or for loops. Instead there are only tags. Some tags are replaced with a value, some nothing, and others a series of values.</span>
  </a><a class="result" href="/passenger">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1054/icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Passenger</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1211</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Phusion Passenger is a web server and application server, designed to be fast, robust and lightweight. It takes a lot of complexity out of deploying web apps, adds powerful enterprise-grade features that are useful in production, and makes administration much easier and less complex.</span>
  </a><a class="result" href="/jquery-mobile">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1023/80508321d8ce3ba8aa264380bb7eba33_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">jQuery Mobile</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1161</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">jQuery Mobile is a HTML5-based user interface system designed to make responsive web sites and apps that are accessible on all smartphone, tablet and desktop devices.</span>
  </a><a class="result" href="/highcharts">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1435/Vx4_Psj1.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Highcharts</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">783</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Highcharts currently supports line, spline, area, areaspline, column, bar, pie, scatter, angular gauges, arearange, areasplinerange, columnrange, bubble, box plot, error bars, funnel, waterfall and polar chart types.</span>
  </a><a class="result" href="/sidekiq">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1078/4b7277462dadad85454ab427ce3f0ca7.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sidekiq</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">513</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Sidekiq uses threads to handle many jobs at the same time in the same process. It does not require Rails but will integrate tightly with Rails 3/4 to make background processing dead simple.</span>
  </a><a class="result" href="/pandas">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2180/1284191.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Pandas</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">153</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more.</span>
  </a><a class="result" href="/hibernate">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1756/1uNl_IZX.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Hibernate</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">162</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Hibernate is a suite of open source projects around domain models. The flagship project is Hibernate ORM, the Object Relational Mapper.</span>
  </a><a class="result" href="/materialize">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2015/GN559Lfb.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Materialize</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">64</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A CSS Framework based on material design.</span>
  </a><a class="result" href="/hugo">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1158/hugo-icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Hugo</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">233</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Hugo is a static site generator written in Go. It is optimized for speed, easy use and configurability. Hugo takes a directory with content and templates and renders them into a full html website. Hugo makes use of markdown files with front matter for meta data.</span>
  </a><a class="result" href="/groovy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/997/6d180ca6647e7f690c2615a86e7c2843.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Groovy</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">369</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Groovy builds upon the strengths of Java but has additional power features inspired by languages like Python, Ruby and Smalltalk. It makes modern programming features available to Java developers with almost-zero learning curve.</span>
  </a><a class="result" href="/neo4j">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1482/FbkjM42a.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Neo4j</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">184</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Neo4j stores data in nodes connected by directed, typed relationships with properties on both, also known as a Property Graph. It is a high performance graph store with all the features expected of a mature and robust database, like a friendly query language and ACID transactions.</span>
  </a><a class="result" href="/plesk">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1663/x65RF1Rg_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Plesk</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1461</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Build and manage multiple sites from a single dashboard. You can also run updates, monitor performance and onboard new prospects all from the same place. It is a WebOps platform to run, automate and grow applications, websites and hosting businesses. </span>
  </a><a class="result" href="/vuetify">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6163/PzNbCwXH.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Vuetify</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">91</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Vuetify is a component framework for Vue.js 2. It aims to provide clean, semantic and reusable components that make building your application a breeze. Vuetify utilizes Google's Material Design design pattern, taking cues from other popular frameworks such as Materialize.css, Material Design Lite, Semantic UI and Bootstrap 4.</span>
  </a><a class="result" href="/google-bigquery">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/695/BigQuery.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google BigQuery</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">304</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Run super-fast, SQL-like queries against terabytes of data in seconds, using the processing power of Google's infrastructure.
Load data with ease. Bulk load your data using Google Cloud Storage or stream it in.
Easy access. Access BigQuery by using a browser tool, a command-line tool, or by making calls to the BigQuery REST API with client libraries such as Java, PHP or Python.</span>
  </a><a class="result" href="/haskell">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1069/oCgm29k9.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Haskell</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">101</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional"></span>
  </a><a class="result" href="/ios">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2886/ios-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">iOS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">55</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the operating system that presently powers many of the mobile devices, including the iPhone, iPad, and iPod Touch. It is designed to make your iPhone and iPad experience even faster, more responsive, and more delightful.</span>
  </a><a class="result" href="/google-kubernetes-engine">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1587/s01TMTGn.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Kubernetes Engine</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">346</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Container Engine takes care of provisioning and maintaining the underlying virtual machine cluster, scaling your application, and operational logistics like logging, monitoring, and health management.</span>
  </a><a class="result" href="/nuxt">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7304/23360933.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Nuxt.js</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">174</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Nuxt.js presets all the configuration needed to make your development of a Vue.js application enjoyable.

You can use Nuxt.js for SSR, SPA, Static Generated, PWA and more.</span>
  </a><a class="result" href="/vuex">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6705/6128107.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">vuex</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">127</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Vuex is a state management pattern + library for Vue.js applications. It serves as a centralized store for all the components in an application, with rules ensuring that the state can only be mutated in a predictable fashion. It also integrates with Vue's official devtools extension to provide advanced features such as zero-config time-travel debugging and state snapshot export / import.</span>
  </a><a class="result" href="/asp-net-core">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/11331/asp.net-core.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ASP.NET Core</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">46</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A free and open-source web framework, and higher performance than ASP.NET, developed by Microsoft and the community. It is a modular framework that runs on both the full .NET Framework, on Windows, and the cross-platform .NET Core.</span>
  </a><a class="result" href="/serverless">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5095/serverless-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Serverless</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">255</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Build applications comprised of microservices that run in response to events, auto-scale for you, and only charge you when they run. This lowers the total cost of maintaining your apps, enabling you to build more logic, faster. The Framework uses new event-driven compute services, like AWS Lambda, Google CloudFunctions, and more.</span>
  </a><a class="result" href="/create-react-app">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5537/oi64YzXY.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Create React App</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">50</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Create React apps with no build configuration.</span>
  </a><a class="result" href="/influxdb">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1396/fc3a45a16c93d59408e04097e8bef1e8.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">InfluxDB</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">199</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">InfluxDB is a scalable datastore for metrics, events, and real-time analytics. It has a built-in HTTP API so you don't have to write any server side code to get up and running.

InfluxDB is designed to be scalable, simple to install and manage, and fast to get data in and out.</span>
  </a><a class="result" href="/apache-cordova">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1716/cordova_256.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache Cordova</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">166</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Apache Cordova is a set of device APIs that allow a mobile app developer to access native device function such as the camera or accelerometer from JavaScript. Combined with a UI framework such as jQuery Mobile or Dojo Mobile or Sencha Touch, this allows a smartphone app to be developed with just HTML, CSS, and JavaScript.</span>
  </a><a class="result" href="/gunicorn">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1091/gunicorn.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gunicorn</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">368</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Gunicorn is a pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.</span>
  </a><a class="result" href="/akka">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1773/bxLhidly.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Akka</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">126</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Akka is a toolkit and runtime for building highly concurrent, distributed, and resilient message-driven applications on the JVM.</span>
  </a><a class="result" href="/elementor">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9785/ANnL6CuP_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Elementor</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1265</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Create beautiful websites using a simple, intuitive drag and drop Interface.It offers pixel perfect design, yet produces 100% clean code. Take your design vision and turn it into a stunning custom-made website. It's fast and easy.</span>
  </a><a class="result" href="/phoenix-framework">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3262/-s9uoLIN.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Phoenix Framework</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">118</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Phoenix is a framework for building HTML5 apps, API backends and distributed systems. Written in Elixir, you get beautiful syntax, productive tooling and a fast runtime.</span>
  </a><a class="result" href="/js-chart">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3866/_GD1-XrU_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Chart.js</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">876</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Visualize your data in 6 different ways. Each of them animated, with a load of customisation options and interactivity extensions.</span>
  </a><a class="result" href="/lua">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2118/128px-Lua-Logo.svg.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Lua</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">293</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Lua combines simple procedural syntax with powerful data description constructs based on associative arrays and extensible semantics. Lua is dynamically typed, runs by interpreting bytecode for a register-based virtual machine, and has automatic memory management with incremental garbage collection, making it ideal for configuration, scripting, and rapid prototyping.</span>
  </a><a class="result" href="/ant-design">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6112/12101536.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Ant Design</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">152</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">An enterprise-class UI design language and React-based implementation. Graceful UI components out of the box, base on React Component. A npm + webpack + babel + dora + dva development framework.</span>
  </a><a class="result" href="/nativescript">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2605/_fBe-iYT.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">NativeScript</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">25</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">NativeScript enables developers to build native apps for iOS, Android and Windows Universal while sharing the application code across the platforms. When building the application UI, developers use our libraries, which abstract the differences between the native platforms.</span>
  </a><a class="result" href="/powershell">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3681/powershell-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PowerShell</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">353</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A command-line shell and scripting language built on .NET. Helps system administrators and power-users rapidly automate tasks that manage operating systems (Linux, macOS, and Windows) and processes. </span>
  </a><a class="result" href="/ionicons">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5368/icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Ionicons</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1157</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Premium designed icons for use in web, iOS, Android, and desktop apps. Support for SVG and web font. Completely open source and MIT licensed.</span>
  </a><a class="result" href="/linode">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/24/631d437cd8e04903f69766a85d8a5540.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Linode</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">167</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Get a server running in minutes with your choice of Linux distro, resources, and node location.</span>
  </a><a class="result" href="/prettier">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7035/icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Prettier</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">484</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Prettier is an opinionated code formatter. It enforces a consistent style by parsing your code and re-printing it with its own rules that take the maximum line length into account, wrapping code when necessary.</span>
  </a><a class="result" href="/numpy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2179/preview.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">NumPy</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">178</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.</span>
  </a><a class="result" href="/datatables">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5693/7730351a5c782c7e25523388bfa8e393_400x400.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">DataTables</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1029</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a highly flexible tool, built upon the foundations of progressive enhancement, that adds all of these advanced features to any HTML table.</span>
  </a><a class="result" href="/mootools">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5991/mootools.twitter_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">MooTools</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1164</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a collection of JavaScript utilities designed for the intermediate to advanced JavaScript developer. It allows you to write powerful and flexible code with its elegant, well documented, and coherent APIs.</span>
  </a><a class="result" href="/nestjs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8747/4zsOyxko_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">NestJS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">90</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Nest is a framework for building efficient, scalable Node.js server-side applications. It uses progressive JavaScript, is built with TypeScript (preserves compatibility with pure JavaScript) and combines elements of OOP (Object Oriented Programming), FP (Functional Programming), and FRP (Functional Reactive Programming).

Under the hood, Nest makes use of Express, but also, provides compatibility with a wide range of other libraries, like e.g. Fastify, allowing for easy use of the myriad third-party plugins which are available.</span>
  </a><a class="result" href="/amazon-ebs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/231/amazon-ebs.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon EBS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">243</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon EBS volumes are network-attached, and persist independently from the life of an instance. Amazon EBS provides highly available, highly reliable, predictable storage volumes that can be attached to a running Amazon EC2 instance and exposed as a device within the instance. Amazon EBS is particularly suited for applications that require a database, file system, or access to raw block level storage.</span>
  </a><a class="result" href="/pusher">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/115/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Pusher</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">172</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Pusher is the category leader in delightful APIs for app developers building communication and collaboration features.</span>
  </a><a class="result" href="/phonegap">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/777/NgaEDjHt.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PhoneGap</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">120</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">PhoneGap is a web platform that exposes native mobile device apis and data to JavaScript. PhoneGap is a distribution of Apache Cordova. PhoneGap allows you to use standard web technologies such as HTML5, CSS3, and JavaScript for cross-platform development, avoiding each mobile platforms' native development language. Applications execute within wrappers targeted to each platform, and rely on standards-compliant API bindings to access each device's sensors, data, and network status.</span>
  </a><a class="result" href="/play">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1013/HqN22PuY.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Play</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">287</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Play Framework makes it easy to build web applications with Java &amp; Scala. Play is based on a lightweight, stateless, web-friendly architecture. Built on Akka, Play provides predictable and minimal resource consumption (CPU, memory, threads) for highly-scalable applications.</span>
  </a><a class="result" href="/unity-3d">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2084/CGKUrcD9_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Unity</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">93</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Unity is the ultimate game development platform. Use Unity to build high-quality 3D and 2D games, deploy them across mobile, desktop, VR/AR, consoles or the Web, and connect with loyal and enthusiastic players and customers.</span>
  </a><a class="result" href="/grpc">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4670/Tb-g6Nu3_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">gRPC</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">126</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">gRPC is a modern open source high performance RPC framework that can run in any environment. It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking...</span>
  </a><a class="result" href="/erlang">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1004/cbdf77412da183e43d41c0c0f9a7005a.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Erlang</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">161</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Some of Erlang's uses are in telecoms, banking, e-commerce, computer telephony and instant messaging. Erlang's runtime system has built-in support for concurrency, distribution and fault tolerance. OTP is set of Erlang libraries and design principles providing middle-ware to develop these systems.</span>
  </a><a class="result" href="/rxjs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1796/984368.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">RxJS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">251</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">RxJS is a library for reactive programming using Observables, to make it easier to compose asynchronous or callback-based code. This project is a rewrite of Reactive-Extensions/RxJS with better performance, better modularity, better debuggable call stacks, while staying mostly backwards compatible, with some breaking changes that reduce the API surface.</span>
  </a><a class="result" href="/amazon-rds-for-postgresql">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/434/amazon-rds.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon RDS for PostgreSQL</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">275</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon RDS manages complex and time-consuming administrative tasks such as PostgreSQL software installation and upgrades, storage management, replication for high availability and back-ups for disaster recovery. With just a few clicks in the AWS Management Console, you can deploy a PostgreSQL database with automatically configured database parameters for optimal performance. Amazon RDS for PostgreSQL database instances can be provisioned with either standard storage or Provisioned IOPS storage. Once provisioned, you can scale from 10GB to 3TB of storage and from 1,000 IOPS to 30,000 IOPS. </span>
  </a><a class="result" href="/sequelize">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3211/3591786.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sequelize</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">70</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Sequelize is a promise-based ORM for Node.js and io.js. It supports the dialects PostgreSQL, MySQL,
MariaDB, SQLite and MSSQL and features solid transaction support, relations, read replication and
more.</span>
  </a><a class="result" href="/adobe-xd">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5602/adobe-xd-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Adobe XD</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">111</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A vector-based tool developed and published by Adobe Inc for designing and prototyping user experience for web and mobile apps. </span>
  </a><a class="result" href="/elm">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4009/cZHhsF-c_normal.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Elm</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">70</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Writing HTML apps is super easy with elm-lang/html. Not only does it render extremely fast, it also quietly guides you towards well-architected code.</span>
  </a><a class="result" href="/composer">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1688/New_Project__65_.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Composer</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">189</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a tool for dependency management in PHP. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.</span>
  </a><a class="result" href="/activemq">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1062/vlz__1_.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ActiveMQ</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">66</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Apache ActiveMQ is fast, supports many Cross Language Clients and Protocols, comes with easy to use Enterprise Integration Patterns and many advanced features while fully supporting JMS 1.1 and J2EE 1.4. Apache ActiveMQ is released under the Apache 2.0 License.</span>
  </a><a class="result" href="/react-redux">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7374/react-redux.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">React Redux</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">31</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the official React binding for Redux. It lets your React components read data from a Redux store, and dispatch actions to the store to update data. It is designed to work with React's component model. You define how to extract the values your component needs from Redux, and your component receives them as props.</span>
  </a><a class="result" href="/styled-components">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6749/styled-components.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">styled-components</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">321</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Visual primitives for the component age. Use the best bits of ES6 and CSS to style your apps without stress 💅</span>
  </a><a class="result" href="/angular-cli">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5527/9kVhSQ9y_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Angular CLI</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">51</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A command-line interface tool that you use to initialize, develop, scaffold, and maintain Angular applications. You can use the tool directly in a command shell, or indirectly through an interactive UI such as Angular Console.</span>
  </a><a class="result" href="/sinatra">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/999/logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sinatra</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">122</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Sinatra is a DSL for quickly creating web applications in Ruby with minimal effort.</span>
  </a><a class="result" href="/mongodb-atlas">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5739/atlas-360x360.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">MongoDB Atlas</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">117</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">MongoDB Atlas is a global cloud database service built and run by the team behind MongoDB. Enjoy the flexibility and scalability of a document database, with the ease and automation of a fully managed service on your preferred cloud.</span>
  </a><a class="result" href="/material-design-lite">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3318/I7ZBJ4-L.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Material Design Lite</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">459</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Material Design Lite (MDL) lets you add a Material Design look and feel to your static content websites. It doesn't rely on any JavaScript frameworks or libraries. Optimized for cross-device use, gracefully degrades in older browsers, and offers an experience that is accessible from the get-go.</span>
  </a><a class="result" href="/gnu-bash">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1673/bash-icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GNU Bash</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">124</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The Bourne Again SHell is an sh-compatible shell that incorporates useful features from the Korn shell (ksh) and C shell (csh). It is intended to conform to the IEEE POSIX P1003.2/ISO 9945.2 Shell and Tools standard.</span>
  </a><a class="result" href="/azure-storage">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2099/azure-storage.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Azure Storage</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">138</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Azure Storage provides the flexibility to store and retrieve large amounts of unstructured data, such as documents and media files with Azure Blobs; structured nosql based data with Azure Tables; reliable messages with Azure Queues, and use SMB based Azure Files for migrating on-premises applications to the cloud.</span>
  </a><a class="result" href="/metabase">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3860/4unoiuHt_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Metabase</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">154</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an easy way to generate charts and dashboards, ask simple ad hoc queries without using SQL, and see detailed information about rows in your Database. You can set it up in under 5 minutes, and then give yourself and others a place to ask simple questions and understand the data your application is generating.</span>
  </a><a class="result" href="/uikit">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1107/2247444e82685c05034fc296fc331472.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">UIkIt</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">532</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">UIkit gives you a comprehensive collection of HTML, CSS, and JS components
which is simple to use, easy to customize and extendable.</span>
  </a><a class="result" href="/material-design">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3994/guidelines-icon-192x192.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Material Design</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">55</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Material Design is a unified system that combines theory, resources, and tools for crafting digital experiences.</span>
  </a><a class="result" href="/unicorn">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1053/unicorn.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Unicorn</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">209</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Unicorn is an HTTP server for Rack applications designed to only serve fast clients on low-latency, high-bandwidth connections and take advantage of features in Unix/Unix-like kernels. Slow clients should only be served by placing a reverse proxy capable of fully buffering both the the request and response in between Unicorn and slow clients.</span>
  </a></div>
</body>
</html>
"""

bs = BeautifulSoup(html, 'lxml')

result = bs.find_all('img')
#print(result)
#print(str(result))
#result2 = bs.find_all('span', class_="additional-name")
#print(result2)
#print(len(result2))
#print(type(table))

results = []
results2 = []
a = 0
for data in result:
    #print(data)
    a = a + 1
    results2.append(a)
    results.append(data)

#print(results)
#print(type(results))

data = pd.DataFrame([results, results2])
print(type(data))
#print(data)
data.to_csv('C:/Users/i9i91/OneDrive/바탕 화면/github 저장내용/portfolio.io/크롤링22.csv')  




