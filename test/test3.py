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
<div class="totals total-all text-right">260 results</div>
<a class="result" href="/devops-automation-for-sql-server">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/11275/devopsdata.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">DevOps Automation for SQL Server</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">0</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It minimizes deployment risks, energizes quality and update frequency, makes the overall workflow consistent and safe. It is a cutting-edge solution that takes conventional database development and deployment to a whole new level.</span>
  </a><a class="result" href="/azure-devops">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4313/XNKktHjN_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Azure DevOps</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">224</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Azure DevOps provides unlimited private Git hosting, cloud build for continuous integration, agile planning, and release management for continuous delivery to the cloud and on-premises.  Includes broad IDE support.</span>
  </a><a class="result" href="/azure-devops-server">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4414/BpqlqOrE_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Azure DevOps Server</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">36</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is set of collaborative software development tools, hosted on-premises. It integrates with your existing IDE or editor, enabling your cross-functional team to work effectively on projects of all sizes.</span>
  </a><a class="result" href="/toad-devops-toolkit">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/12194/toadDev.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Toad DevOps Toolkit</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">0</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It makes it easy to integrate Oracle database change management into your DevOps workflow — without compromising quality, performance or reliability. Toad DevOps Toolkit works in conjunction with automation tools like Jenkins, Bamboo and Team Foundation Server to include database development and deployment steps as part of your existing CI/CD processes — removing the database bottleneck and speeding project completion.</span>
  </a><a class="result" href="/apexsql-devops-toolkit">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/12193/Wqt9ju1O_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ApexSQL DevOps toolkit</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">0</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It enables users to create flexible CI and CD pipelines with highly customizable pipeline steps. These steps include: Build, Populate, Audit, Document, Test, Review, Package, Schema sync, Data sync, Deploy, Notify and Publish.</span>
  </a><a class="result" href="/compliant-database-devops">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/12192/compliant.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Compliant Database DevOps</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">0</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It gives you an end-to-end framework for extending DevOps to your database while complying with regulations and protecting your data.</span>
  </a><a class="result" href="/github">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/27/sBsvBbjY.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GitHub</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7871</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">GitHub is the best place to share code with friends, co-workers, classmates, and complete strangers. Over three million people use GitHub to build amazing things together.</span>
  </a><a class="result" href="/git">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1046/git.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Git</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6553</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.</span>
  </a><a class="result" href="/docker">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/586/n4u37v9t_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Docker</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7190</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The Docker Platform is the industry-leading container platform for continuous, high-velocity innovation, enabling organizations to seamlessly build and share any application — from legacy to what comes next  — and securely run them anywhere</span>
  </a><a class="result" href="/visual-studio-code">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4202/Visual_Studio_Code_logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Visual Studio Code</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2410</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Build and debug modern web and cloud applications. Code is free and available on your favorite platform - Linux, Mac OSX, and Windows.</span>
  </a><a class="result" href="/npm">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1120/lejvzrnlpb308aftn31u.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">npm</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4361</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">npm is the command-line interface to the npm ecosystem. It is battle-tested, surprisingly flexible, and used by hundreds of thousands of JavaScript developers every day.</span>
  </a><a class="result" href="/jenkins">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/670/jenkins.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Jenkins</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2848</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">In a nutshell Jenkins CI is the leading open-source continuous integration server. Built with Java, it provides over 300 plugins to support building and testing virtually any project.</span>
  </a><a class="result" href="/gitlab">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/880/lmalkclL.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GitLab</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2338</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">GitLab offers git repository management, code reviews, issue tracking, activity feeds and wikis. Enterprises install GitLab on-premise and connect it with LDAP and Active Directory servers for secure authentication and authorization. A single GitLab server can handle more than 25,000 users but it is also possible to create a high availability setup with multiple active servers.</span>
  </a><a class="result" href="/bitbucket">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/28/35O2KIRX_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bitbucket</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2776</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Bitbucket gives teams one place to plan projects, collaborate on code, test and deploy, all with free private Git repositories. Teams choose Bitbucket because it has a superior Jira integration, built-in CI/CD, &amp; is free for up to 5 users.</span>
  </a><a class="result" href="/kubernetes">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1885/21_d3cvM.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Kubernetes</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2093</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Kubernetes is an open source orchestration system for Docker containers. It handles scheduling onto nodes in a compute cluster and actively manages workloads to ensure that their state matches the users declared intentions.</span>
  </a><a class="result" href="/sublime-text">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/642/SublimeText_Master_012312_icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sublime Text</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1968</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Sublime Text is available for OS X, Windows and Linux. One license is all you need to use Sublime Text on every computer you own, no matter what operating system it uses.

Sublime Text uses a custom UI toolkit, optimized for speed and beauty, while taking advantage of native functionality on each platform.</span>
  </a><a class="result" href="/webpack">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1682/IMG_4636.PNG">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Webpack</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3714</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows to load parts for the application on demand. Through "loaders" modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff.</span>
  </a><a class="result" href="/visual-studio">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1451/SR2hUhQN.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Visual Studio</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1203</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Visual Studio is a suite of component-based software development tools and other technologies for building powerful, high-performance applications.</span>
  </a><a class="result" href="/intellij-idea">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1453/icon_IntelliJIDEA.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">IntelliJ IDEA</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1374</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Out of the box, IntelliJ IDEA provides a comprehensive feature set including tools and integrations with the most important modern technologies and frameworks for enterprise and web development with Java, Scala, Groovy and other languages.</span>
  </a><a class="result" href="/virtualbox">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/774/vbox_94px.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">VirtualBox</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1078</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use. Not only is VirtualBox an extremely feature rich, high performance product for enterprise customers, it is also the only professional solution that is freely available as Open Source Software under the terms of the GNU General Public License (GPL) version 2.</span>
  </a><a class="result" href="/modernizr">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2440/9TeXWBzR_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Modernizr</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">24157</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It’s a collection of superfast tests or detects as we like to call them which run as your web page loads, then you can use the results to tailor the experience to the user. It tells you what HTML, CSS and JavaScript features the user’s browser has to offer.</span>
  </a><a class="result" href="/vim">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/644/vim_logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Vim</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1296</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Vim is an advanced text editor that seeks to provide the power of the de-facto Unix editor 'Vi', with a more complete feature set. Vim is a highly configurable text editor built to enable efficient text editing. It is an improved version of the vi editor distributed with most UNIX systems. Vim is distributed free as charityware. </span>
  </a><a class="result" href="/new-relic">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/103/yEDRfH2o.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">New Relic</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">11528</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">New Relic is the all-in-one web application performance tool that lets you see performance from the end user experience, through servers, and down to the line of application code.</span>
  </a><a class="result" href="/android-studio">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1447/AyreX9yf.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Android Studio</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1548</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Android Studio is a new Android development environment based on IntelliJ IDEA. It provides new features and improvements over Eclipse ADT and will be the official Android IDE once it's ready.</span>
  </a><a class="result" href="/atom">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/648/QbnVqgX4.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Atom</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1142</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">At GitHub, we're building the text editor we've always wanted. A tool you can customize to do anything, but also use productively on the first day without ever touching a config file. Atom is modern, approachable, and hackable to the core. We can't wait to see what you build with it.</span>
  </a><a class="result" href="/pycharm">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1644/logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PyCharm</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">676</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">PyCharm’s smart code editor provides first-class support for Python, JavaScript, CoffeeScript, TypeScript, CSS, popular template languages and more. Take advantage of language-aware code completion, error detection, and on-the-fly code fixes!</span>
  </a><a class="result" href="/ansible">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/663/ElOjna20.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Ansible</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1541</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates. Ansible’s goals are foremost those of simplicity and maximum ease of use.</span>
  </a><a class="result" href="/xcode">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1448/xcode.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Xcode</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1673</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The Xcode IDE is at the center of the Apple development experience. Tightly integrated with the Cocoa and Cocoa Touch frameworks, Xcode is an incredibly productive environment for building amazing apps for Mac, iPhone, and iPad.</span>
  </a><a class="result" href="/docker-compose">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3136/docker-compose.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Docker Compose</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1383</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With Compose, you define a multi-container application in a single file, then spin your application up in a single command which does everything that needs to be done to get it running.</span>
  </a><a class="result" href="/kibana">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1722/Image_2019-05-20_at_4.53.31_PM.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Kibana</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1486</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Kibana is an open source (Apache Licensed), browser based analytics and search dashboard for Elasticsearch. Kibana is a snap to setup and start using. Kibana strives to be easy to get started with, while also being flexible and powerful, just like Elasticsearch.</span>
  </a><a class="result" href="/notepad-plus-plus">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/646/logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Notepad++</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">351</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Notepad++ is a free (as in "free speech" and also as in "free beer") source code editor and Notepad replacement that supports several languages. Running in the MS Windows environment, its use is governed by GPL License.</span>
  </a><a class="result" href="/gulp">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/844/iruTC031.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">gulp</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1726</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Build system automating tasks: minification and copying of all JavaScript files, static images. More capable of watching files to automatically rerun the task when a file changes.</span>
  </a><a class="result" href="/babel">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2739/-1wfGjNw.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Babel</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1912</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Babel will turn your ES6+ code into ES5 friendly code, so you can start using it right now without waiting for browser support.</span>
  </a><a class="result" href="/yarn">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5848/44mC-kJ3.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Yarn</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1579</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Yarn caches every package it downloads so it never needs to again. It also parallelizes operations to maximize resource utilization so install times are faster than ever.</span>
  </a><a class="result" href="/selenium">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1517/sbUizSli_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Selenium</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1199</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Selenium automates browsers. That's it! What you do with that power is entirely up to you. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) also be automated as well.</span>
  </a><a class="result" href="/phpstorm">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1452/icon_PhpStorm.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PhpStorm</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1051</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">PhpStorm is a PHP IDE which keeps up with latest PHP &amp; web languages trends, integrates a variety of modern tools, and brings even more extensibility with support for major PHP frameworks.</span>
  </a><a class="result" href="/eslint">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3337/Q4L7Jncy.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ESLint</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1574</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A pluggable and configurable linter tool for identifying and reporting on patterns in JavaScript. Maintain your code quality with ease.</span>
  </a><a class="result" href="/sentry">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/191/lzoDXqf-.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sentry</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2911</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Sentry is an open-source platform for workflow productivity, aggregating errors from across the stack in real time. 500K developers use Sentry to get the code-level context they need to resolve issues at every stage of the app lifecycle.</span>
  </a><a class="result" href="/varnish">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1073/mPwTb3BF.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Varnish</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">9213</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Varnish Cache is a web application accelerator also known as a caching HTTP reverse proxy. You install it in front of any server that speaks HTTP and configure it to cache the contents. Varnish Cache is really, really fast. It typically speeds up delivery with a factor of 300 - 1000x, depending on your architecture.</span>
  </a><a class="result" href="/vagrant">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/768/150px-Vagrant.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Vagrant</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1152</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Vagrant provides the framework and configuration format to create and manage complete portable development environments. These development environments can live on your computer or in the cloud, and are portable between Windows, Mac OS X, and Linux.</span>
  </a><a class="result" href="/travis-ci">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/460/Lu6cGu0z_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Travis CI</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1464</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Free for open source projects, our CI environment provides multiple runtimes (e.g. Node.js or PHP versions), data stores and so on. Because of this, hosting your project on travis-ci.com means you can effortlessly test your library or applications against multiple runtimes and data stores without even having all of them installed locally.</span>
  </a><a class="result" href="/webstorm">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1455/icon_WebStorm.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">WebStorm</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">797</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">WebStorm is a lightweight and intelligent IDE for front-end development and server-side JavaScript.</span>
  </a><a class="result" href="/sourcetree">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1599/sourcetree.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">SourceTree</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">957</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Use the full capability of Git and Mercurial in the SourceTree desktop app. Manage all your repositories, hosted or local, through SourceTree's simple interface.</span>
  </a><a class="result" href="/grafana">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2645/rhtKuA9t.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Grafana</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1127</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Grafana is a general purpose dashboard and graph composer. It's focused on providing rich ways to visualize time series metrics, mainly though graphs but supports other ways to visualize data through a pluggable panel architecture. It currently has rich support for for Graphite, InfluxDB and OpenTSDB. But supports other data sources via plugins.</span>
  </a><a class="result" href="/terraform">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1276/terraform.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Terraform</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1050</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With Terraform, you describe your complete infrastructure as code, even as it spans multiple service providers. Your servers may come from AWS, your DNS may come from CloudFlare, and your database may come from Heroku. Terraform will build all these resources across all these providers in parallel.</span>
  </a><a class="result" href="/circleci">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/190/CvqrSSFs_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">CircleCI</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1636</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Continuous integration and delivery platform helps software teams rapidly release code with confidence by automating the build, test, and deploy process. Offers a modern software development platform that lets teams ramp.</span>
  </a><a class="result" href="/gradle">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/975/gradlephant-social-black-bg.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gradle</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">911</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Gradle is a build tool with a focus on build automation and support for multi-language development. If you are building, testing, publishing, and deploying software on any platform, Gradle offers a flexible model that can support the entire development lifecycle from compiling and packaging code to publishing web sites.</span>
  </a><a class="result" href="/logstash">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1683/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Logstash</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">923</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Logstash is a tool for managing events and logs. You can use it to collect logs, parse them, and store them for later use (like, for searching). If you store them in Elasticsearch, you can view and analyze them with Kibana.</span>
  </a><a class="result" href="/aws-elastic-load-balancing">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2587/aws-elastic-load-balancing.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS Elastic Load Balancing (ELB)</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1183</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With Elastic Load Balancing, you can add and remove EC2 instances as your needs change without disrupting the overall flow of information. If one EC2 instance fails, Elastic Load Balancing automatically reroutes the traffic to the remaining running EC2 instances. If the failed EC2 instance is restored, Elastic Load Balancing restores the traffic to that instance. Elastic Load Balancing offers clients a single point of contact, and it can also serve as the first line of defense against attacks on your network. You can offload the work of encryption and decryption to Elastic Load Balancing, so your servers can focus on their main task.</span>
  </a><a class="result" href="/amazon-cloudwatch">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/401/amazon-cloudwatch.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon CloudWatch</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1226</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It helps you gain system-wide visibility into resource utilization, application performance, and operational health. It retrieve your monitoring data, view graphs to help take automated action based on the state of your cloud environment.</span>
  </a><a class="result" href="/grunt">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/845/falgg2jybmhgk16y62lr.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Grunt</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1097</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The less work you have to do when performing repetitive tasks like minification, compilation, unit testing, linting, etc, the easier your job becomes. After you've configured it, a task runner can do most of that mundane work for you—and your team—with basically zero effort.</span>
  </a><a class="result" href="/bower">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/847/66db62603f426a8fc6664081811be6d4.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bower</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1090</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Bower is a package manager for the web. It offers a generic, unopinionated solution to the problem of front-end package management, while exposing the package dependency model via an API that can be consumed by a more opinionated build stack. There are no system wide dependencies, no dependencies are shared between different apps, and the dependency tree is flat.</span>
  </a><a class="result" href="/requirejs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/852/1781835.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">RequireJS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4476</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">RequireJS loads plain JavaScript files as well as more defined modules. It is optimized for in-browser use, including in a Web Worker, but it can be used in other JavaScript environments, like Rhino and Node. It implements the Asynchronous Module API. Using a modular script loader like RequireJS will improve the speed and quality of your code.</span>
  </a><a class="result" href="/datadog">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/669/5cX1R9Rr_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Datadog</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">881</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Datadog is the leading service for cloud-scale monitoring. It is used by IT, operations, and development teams who build and operate applications that run on dynamic or hybrid cloud infrastructure. Start monitoring in minutes with Datadog!</span>
  </a><a class="result" href="/mocha">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/832/mocha.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mocha</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">674</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Mocha is a feature-rich JavaScript test framework running on node.js and the browser, making asynchronous testing simple and fun. Mocha tests run serially, allowing for flexible and accurate reporting, while mapping uncaught exceptions to the correct test cases. </span>
  </a><a class="result" href="/jest">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/830/jest.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Jest</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">938</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Jest provides you with multiple layers on top of Jasmine.</span>
  </a><a class="result" href="/browserstack">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/182/0pyDMTyp.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">BrowserStack</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">810</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Live, Web-Based Browser Testing
Instant access to all real mobile and desktop browsers. Say goodbye to your lab of devices and virtual machines.</span>
  </a><a class="result" href="/pingdom">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/106/usvDLKsY_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Pingdom</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1092</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Pingdom is an uptime monitoring service. When problems happen with a site that Pingdom monitors, it immediately alerts the owner so the problem can be taken care of.</span>
  </a><a class="result" href="/haproxy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1179/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">HAProxy</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">667</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">HAProxy (High Availability Proxy) is a free, very fast and reliable solution offering high availability, load balancing, and proxying for TCP and HTTP-based applications.</span>
  </a><a class="result" href="/trackjs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1122/logo_icon_white_charcoal_onred_1000.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">TrackJS</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3186</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Production error monitoring and reporting for web applications. TrackJS provides deep insights into real user errors. See the user, network, and application events that tell the story of an error so you can actually fix them.</span>
  </a><a class="result" href="/eclipse">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1446/8cyY6D_m.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Eclipse</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">366</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Standard Eclipse package suited for Java and plug-in development plus adding new plugins; already includes Git, Marketplace Client, source code and developer documentation. 
Click here to file a bug against Eclipse Platform.</span>
  </a><a class="result" href="/prometheus">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2501/prometheus.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Prometheus</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">549</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Prometheus is a systems and service monitoring system. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts if some condition is observed to be true.</span>
  </a><a class="result" href="/maven">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/977/maven.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache Maven</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">506</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Maven allows a project to build using its project object model (POM) and a set of plugins that are shared by all projects using Maven, providing a uniform build system. Once you familiarize yourself with how one Maven project builds you automatically know how all Maven projects build saving you immense amounts of time when trying to navigate many projects.</span>
  </a><a class="result" href="/yeoman">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/853/46ea2dd8b1bdd31a8ba61044cb5b6ebe.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Yeoman</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">285</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Yeoman is a robust and opinionated set of tools, libraries, and a workflow that can help developers quickly build beautiful, compelling web apps. It is comprised of yo - a scaffolding tool using our generator system, grunt - a task runner for your build process and bower for dependency management.</span>
  </a><a class="result" href="/rollbar">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/328/IWsbTBOs_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Rollbar</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">631</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Rollbar helps development teams find and fix errors faster. Quickly pinpoint what’s broken and why. View exceptions from all of your languages, frameworks, platforms &amp; environments in one place. Get context &amp; insights to defeat all errors.</span>
  </a><a class="result" href="/gitlab-ci">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5545/9pAwHBR0.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GitLab CI</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">483</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">GitLab offers a continuous integration service. If you add a .gitlab-ci.yml file to the root directory of your repository, and configure your GitLab project to use a Runner, then each merge request or push triggers your CI pipeline.</span>
  </a><a class="result" href="/aws-cloudformation">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/411/aws-cloudformation.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS CloudFormation</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">337</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">You can use AWS CloudFormation’s sample templates or create your own templates to describe the AWS resources, and any associated dependencies or runtime parameters, required to run your application. You don’t need to figure out the order in which AWS services need to be provisioned or the subtleties of how to make those dependencies work.</span>
  </a><a class="result" href="/chef">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/420/24f4ef5e7a67c0d720bf9ae69dd6de2a.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Chef</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">450</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Chef enables you to manage and scale cloud infrastructure with no downtime or interruptions. Freely move applications and configurations from one cloud to another. Chef is integrated with all major cloud providers including Amazon EC2, VMWare, IBM Smartcloud, Rackspace, OpenStack, Windows Azure, HP Cloud, Google Compute Engine, Joyent Cloud and others.</span>
  </a><a class="result" href="/codeship">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/224/avatar_codeship_colour.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Codeship</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">364</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Codeship runs your automated tests and configured deployment when you push to your repository. It takes care of managing and scaling the infrastructure so that you are able to test and release more frequently and get faster feedback for building the product your users need.</span>
  </a><a class="result" href="/jasmine">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/831/7c0b595409af531b9cdeb07f8c513e8b.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Jasmine</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">218</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Jasmine is a Behavior Driven Development testing framework for JavaScript. It does not rely on browsers, DOM, or any JavaScript framework. Thus it's suited for websites, Node.js projects, or anywhere that JavaScript can run.</span>
  </a><a class="result" href="/testflight">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/95/oGea5QYO.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">TestFlight</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">435</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With TestFlight, developers simply upload a build, and the testers can install it directly from their device, over the air.</span>
  </a><a class="result" href="/capistrano">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/661/5da4e1d78e930197cb7dc002ceafdfda.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Capistrano</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">507</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Capistrano is a remote server automation tool. It supports the scripting and execution of arbitrary tasks, and includes a set of sane-default deployment workflows.</span>
  </a><a class="result" href="/consul">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/747/consul-logo-grad_teaser.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Consul</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">242</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Consul is a tool for service discovery and configuration. Consul is distributed, highly available, and extremely scalable.</span>
  </a><a class="result" href="/emacs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/645/emacs.gif">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Emacs</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">127</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">GNU Emacs is an extensible, customizable text editor—and more. At its core is an interpreter for Emacs Lisp, a dialect of the Lisp programming language with extensions to support text editing. </span>
  </a><a class="result" href="/sonarqube">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2638/zIVhxKyn_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">SonarQube</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">253</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">SonarQube provides an overview of the overall health of your source code and even more importantly, it highlights issues found on new code. With a Quality Gate set on your project, you will simply fix the Leak and start mechanically improving.</span>
  </a><a class="result" href="/teamcity">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1357/317jQkeS.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">TeamCity</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">276</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">TeamCity is a user-friendly continuous integration (CI) server for professional developers, build engineers, and DevOps. It is trivial to setup and absolutely free for small teams and open source projects.</span>
  </a><a class="result" href="/rancher">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2552/rancher.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Rancher</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">150</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Rancher is an open source container management platform that includes full distributions of Kubernetes, Apache Mesos and Docker Swarm, and makes it simple to operate container clusters on any cloud or infrastructure platform.</span>
  </a><a class="result" href="/crashlytics">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/264/Q3LJPRGx.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Crashlytics</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">479</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Instead of just showing you the stack trace, Crashlytics performs deep analysis of each and every thread. We de-prioritize lines that don't matter while highlighting the interesting ones. This makes reading stack traces easier, faster, and far more useful! Crashlytics' intelligent grouping can take 50,000 crashes, distill them down to 20 unique issues, and then tell you which 3 are the most important to fix.</span>
  </a><a class="result" href="/bugsnag">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/150/square-logo-small-midnight.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bugsnag</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">694</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Bugsnag captures errors from your web, mobile and back-end applications, providing instant visibility into user impact.  Diagnostic data and tools are included to help your team prioritize, debug and fix exceptions fast.</span>
  </a><a class="result" href="/nagios">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/786/3gaoi2h254k0canb4hxj.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Nagios</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">231</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Nagios is a host/service/network monitoring program written in C and
released under the GNU General Public License.</span>
  </a><a class="result" href="/puppet">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/421/954f7381089ac290b4690c5ffd9dd7d3.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Puppet Labs</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">246</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Puppet is an automated administrative engine for your Linux, Unix, and Windows systems and performs administrative tasks (such as adding users, installing packages, and updating server configurations) based on a centralized specification.</span>
  </a><a class="result" href="/pagerduty">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/107/GtwgsQj5_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PagerDuty</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">409</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">PagerDuty is an alarm aggregation and dispatching service for system administrators and support teams. It collects alerts from your monitoring tools, gives you an overall view of all of your monitoring alarms, and alerts an on duty engineer if there's a problem.
</span>
  </a><a class="result" href="/docker-swarm">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3177/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Docker Swarm</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">156</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Swarm serves the standard Docker API, so any tool which already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts: Dokku, Compose, Krane, Deis, DockerUI, Shipyard, Drone, Jenkins... and, of course, the Docker client itself.</span>
  </a><a class="result" href="/gitkraken">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4614/XHJt0jRW.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GitKraken</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">90</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The downright luxurious Git client for Windows, Mac and Linux. Cross-platform, 100% standalone, and free.</span>
  </a><a class="result" href="/svn">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1045/svn.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">SVN (Subversion)</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">121</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Subversion exists to be universally recognized and adopted as an open-source, centralized version control system characterized by its reliability as a safe haven for valuable data; the simplicity of its model and usage; and its ability to support the needs of a wide variety of users and projects, from individuals to large-scale enterprise operations.</span>
  </a><a class="result" href="/netbeans">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1449/DxAPXRVS.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">NetBeans IDE</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">85</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">NetBeans IDE is FREE, open source, and has a worldwide community of users and developers.</span>
  </a><a class="result" href="/openstack">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/770/GCPRyAva.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OpenStack</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">96</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">OpenStack is a cloud operating system that controls large pools of compute, storage, and networking resources throughout a datacenter, all managed through a dashboard that gives administrators control while empowering their users to provision resources through a web interface.</span>
  </a><a class="result" href="/cloud9-ide">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/209/CvjNepWX.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Cloud9 IDE</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">48</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Cloud9 provides a development environment in the cloud. Cloud9 enables developers to get started with coding immediately with pre-setup environments called workspaces, collaborate with their peers with collaborative coding features, and build web apps with features like live preview and browser compatibility testing. It supports more than 40 languages, with class A support for PHP, Ruby, Python, JavaScript/Node.js, and Go.</span>
  </a><a class="result" href="/red-hat-codeready-workspaces">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/198/unnamed.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Red Hat Codeready Workspaces</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">16</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Built on the open Eclipse Che project, Red Hat CodeReady Workspaces provides developer workspaces, which include all the tools and the dependencies that are needed to code, build, test, run, and debug applications. </span>
  </a><a class="result" href="/karma-runner">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1420/TidYGd6a.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Karma</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">244</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Karma is not a testing framework, nor an assertion library. Karma just launches a HTTP server, and generates the test runner HTML file you probably already know from your favourite testing framework. So for testing purposes you can use pretty much anything you like. </span>
  </a><a class="result" href="/istio">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7028/AGpa5VZV.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Istio</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">92</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Istio is an open platform for providing a uniform way to integrate microservices, manage traffic flow across microservices, enforce policies and aggregate telemetry data. Istio's control plane provides an abstraction layer over the underlying cluster management platform, such as Kubernetes, Mesos, etc.</span>
  </a><a class="result" href="/zookeeper">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1528/apache-zookeeper.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zookeeper</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">181</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications.</span>
  </a><a class="result" href="/junit">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2020/874086.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">JUnit</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">222</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">JUnit is a simple framework to write repeatable tests. It is an instance of the xUnit architecture for unit testing frameworks.
</span>
  </a><a class="result" href="/papertrail">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/82/papertrail-twitter-128.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Papertrail</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">322</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Papertrail helps detect, resolve, and avoid infrastructure problems using log messages. Papertrail's practicality comes from our own experience as sysadmins, developers, and entrepreneurs.</span>
  </a><a class="result" href="/traefik">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5126/soSblPVT_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Traefik</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">128</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A modern HTTP reverse proxy and load balancer that makes deploying microservices easy. Traefik integrates with your existing infrastructure components and configures itself automatically and dynamically.</span>
  </a><a class="result" href="/helm">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5983/AHcBc6EG_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Helm</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">221</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Helm is the best way to find, share, and use software built for Kubernetes.</span>
  </a><a class="result" href="/cucumber">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2544/jasVAxyJ.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Cucumber</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">140</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Cucumber is a tool that supports Behaviour-Driven Development (BDD) - a software development process that aims to enhance software quality and reduce maintenance costs.</span>
  </a><a class="result" href="/browserify">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/849/9esmqty2.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Browserify</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">172</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Browserify lets you require('modules') in the browser by bundling up all of your dependencies.</span>
  </a><a class="result" href="/kong">
    <div style="display:inline-block">
      <img src="https://ucarecdn.com/3cf09daa-4e1e-404e-a612-f8a91c661db2/">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Kong</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">102</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Kong is a scalable, open source API Layer (also known as an API Gateway, or API Middleware). Kong controls layer 4 and 7 traffic and is extended through Plugins, which provide extra functionality and services beyond the core platform.</span>
  </a><a class="result" href="/rubymine">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1454/icon_RubyMine.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">RubyMine</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">136</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">JetBrains RubyMine IDE provides a comprehensive Ruby code editor aware of dynamic language specifics and delivers smart coding assistance, intelligent code refactoring and code analysis capabilities. </span>
  </a><a class="result" href="/code-climate">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/305/KFgYaUkK.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Code Climate</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">195</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">After each Git push, Code Climate analyzes your code for complexity, duplication, and common smells to determine changes in quality and surface technical debt hotspots.</span>
  </a><a class="result" href="/spring-cloud">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5494/992d3596458fca87741b8e93e7df0860_normal.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Spring Cloud</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">59</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Spring helps development teams everywhere build simple, portable,
fast and flexible JVM-based systems and applications.</span>
  </a><a class="result" href="/github-enterprise">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2900/pBeeJQDQ.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GitHub Enterprise</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">71</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">GitHub Enterprise lets developers use the tools they love across the development process with support for popular IDEs, continuous integration tools, and hundreds of third party apps and services.</span>
  </a><a class="result" href="/brackets">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2226/brackets_512_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Brackets</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">53</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With focused visual tools and preprocessor support, it is a modern text editor that makes it easy to design in the browser. </span>
  </a><a class="result" href="/docker-machine">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3137/fbbb494a7eef5f9278c6967b6072ca3e.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Docker Machine</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">60</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Machine lets you create Docker hosts on your computer, on cloud providers, and inside your own data center. It creates servers, installs Docker on them, then configures the Docker client to talk to them.</span>
  </a><a class="result" href="/packer">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/967/packer.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Packer</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">179</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Packer automates the creation of any type of machine image. It embraces modern configuration management by encouraging you to use automated scripts to install and configure the software within your Packer-made images.</span>
  </a><a class="result" href="/zabbix">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1705/MlkWTc_x.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zabbix</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">87</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Zabbix is a mature and effortless enterprise-class open source monitoring solution for network monitoring and application monitoring of millions of metrics.</span>
  </a><a class="result" href="/elk">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1883/EmPbn9P0_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ELK</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">113</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the acronym for three open source projects: Elasticsearch, Logstash, and Kibana. Elasticsearch is a search and analytics engine. Logstash is a server‑side data processing pipeline that ingests data from multiple sources simultaneously, transforms it, and then sends it to a "stash" like Elasticsearch. Kibana lets users visualize data with charts and graphs in Elasticsearch.

</span>
  </a><a class="result" href="/vault">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2905/vault.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Vault</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">157</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Vault is a tool for securely accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret, while providing tight access control and recording a detailed audit log.</span>
  </a><a class="result" href="/graylog">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4392/_HU28D42.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Graylog</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">122</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Centralize and aggregate all your log files for 100% visibility. Use our powerful query language to search through terabytes of log data to discover and analyze important information.</span>
  </a><a class="result" href="/vmware-vsphere">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/775/c193cd4e31d488620bdd7349ea4836cc.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">VMware vSphere</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">104</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">vSphere is the world’s leading server virtualization platform. Run fewer servers and reduce capital and operating costs using VMware vSphere to build a cloud computing infrastructure.</span>
  </a><a class="result" href="/phantomjs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1832/phantomjs.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PhantomJS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">146</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">PhantomJS (www.phantomjs.org) is a headless WebKit scriptable with JavaScript. It is used by hundreds of developers and dozens of organizations for web-related development workflow.</span>
  </a><a class="result" href="/bamboo">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1729/omsJmyCc.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bamboo</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">113</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Focus on coding and count on Bamboo as your CI and build server! Create multi-stage build plans, set up triggers to start builds upon commits, and assign agents to your critical builds and deployments.</span>
  </a><a class="result" href="/fabric">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/662/79c2d43ca09b8321909833f37a500799.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Fabric</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">196</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Fabric is a Python (2.5-2.7) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.

It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution.</span>
  </a><a class="result" href="/salt">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/664/-lag2uPT.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Salt</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">141</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Salt is a new approach to infrastructure management. Easy enough to get running in minutes, scalable enough to manage tens of thousands of servers, and fast enough to communicate with them in seconds.

Salt delivers a dynamic communication bus for infrastructures that can be used for orchestration, remote execution, configuration management and much more.</span>
  </a><a class="result" href="/enzyme">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4488/enzyme.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Enzyme</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">197</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Enzyme is a JavaScript Testing utility for React that makes it easier to assert, manipulate, and traverse your React Components' output.</span>
  </a><a class="result" href="/aws-codepipeline">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3297/aws-codepipeline.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS CodePipeline</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">73</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">CodePipeline builds, tests, and deploys your code every time there is a code change, based on the release process models you define.</span>
  </a><a class="result" href="/fluentd">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4365/859518.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Fluentd</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">124</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Fluentd collects events from various data sources and writes them to files, RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your logging infrastructure.</span>
  </a><a class="result" href="/sauce-labs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/207/IkgItC1R_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sauce Labs</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">90</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Cloud-based automated testing platform enables developers and QEs to perform functional, JavaScript unit, and manual tests with Selenium or Appium on web and mobile apps. Videos and screenshots for easy debugging. Secure and CI-ready.</span>
  </a><a class="result" href="/graphite">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1050/graphite.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Graphite</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">127</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Graphite does two things: 1) Store numeric time-series data and 2) Render graphs of this data on demand</span>
  </a><a class="result" href="/fastlane">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2383/11098337.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">fastlane</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">179</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">fastlane lets you define and run your deployment pipelines for different environments. It helps you unify your app’s release process and automate the whole process. fastlane connects all fastlane tools and third party tools, like CocoaPods.</span>
  </a><a class="result" href="/portainer">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5926/Qu-iixzV.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Portainer</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">42</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Portainer is an open-source lightweight management UI which allows you to easily manage your Docker environments.

Portainer is available on Windows, Linux and Mac. It has never been so easy to manage Docker !</span>
  </a><a class="result" href="/drone-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/668/R_wMcCqN_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Drone.io</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">85</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Drone is a hosted continuous integration service. It enables you to conveniently set up projects to automatically build, test, and deploy as you make changes to your code.

Drone integrates seamlessly with Github, Bitbucket and Google Code as well as third party services such as Heroku, Dotcloud, Google AppEngine and more.</span>
  </a><a class="result" href="/coveralls">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/680/a43e4a04cb9f778842de43f95db59a14.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Coveralls</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">128</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Coveralls works with your CI server and sifts through your coverage data to find issues you didn't even know you had before they become a problem. Free for open source, pro accounts for private repos, instant sign up with GitHub OAuth.</span>
  </a><a class="result" href="/aws-codecommit">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3298/aws-codecommit.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS CodeCommit</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">44</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">CodeCommit eliminates the need to operate your own source control system or worry about scaling its infrastructure. You can use CodeCommit to securely store anything from source code to binaries, and it works seamlessly with your existing Git tools.</span>
  </a><a class="result" href="/mesos">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/914/d64b637225a3e671799940d5fe13c76b.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache Mesos</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">73</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Apache Mesos is a cluster manager that simplifies the complexity of running applications on a shared pool of servers.</span>
  </a><a class="result" href="/aws-codedeploy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1888/aws-codedeploy.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS CodeDeploy</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">97</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AWS CodeDeploy is a service that automates code deployments to Amazon EC2 instances. AWS CodeDeploy makes it easier for you to rapidly release new features, helps you avoid downtime during deployment, and handles the complexity of updating your applications. </span>
  </a><a class="result" href="/octopus-deploy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1341/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Octopus Deploy</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">84</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Octopus Deploy helps teams to manage releases, automate deployments, and operate applications with automated runbooks. It's free for small teams. </span>
  </a><a class="result" href="/sonatype-nexus">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1847/jnJFp3i1_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sonatype Nexus</span>
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
    <span class="additional">It is an open source repository that supports many artifact formats, including Docker, Java™ and npm. With the Nexus tool integration, pipelines in your toolchain can publish and retrieve versioned apps and their dependencies</span>
  </a><a class="result" href="/codecov">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2673/Codecov_Mark_Circle_Pink.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Codecov</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">131</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Our patrons rave about our elegant coverage reports, integrated pull request comments, interactive commit graphs, our Chrome plugin and security.</span>
  </a><a class="result" href="/codacy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/866/icon-black.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Codacy</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">73</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Codacy automates code reviews to improve and standardize code quality across large enterprises. It identifies issues through static code analysis. Integrates with GitLab, GitHub &amp; Bitbucket.</span>
  </a><a class="result" href="/parcel">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8054/fC6Wad-S_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Parcel</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">303</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Parcel is a web application bundler, differentiated by its developer experience. It offers blazing fast performance utilizing multicore processing, and requires zero configuration.</span>
  </a><a class="result" href="/lambdatest">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8646/gwBrmxMV_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">LambdaTest</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">447</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">LambdaTest is a cloud-based testing platform and it provides access to a powerful network cloud of 2000+ real browsers and operating system that helps testers in cross-browser and cross-platform compatibility testing. </span>
  </a><a class="result" href="/dash">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2405/HB_dh5cX.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Dash</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">42</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Dash is an API Documentation Browser and Code Snippet Manager. Dash stores snippets of code and instantly searches offline documentation sets for 150+ APIs. You can even generate your own docsets or request docsets to be included.</span>
  </a><a class="result" href="/eureka">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2085/99V92_Sr.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Eureka</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">16</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Eureka is a REST (Representational State Transfer) based service that is primarily used in the AWS cloud for locating services for the purpose of load balancing and failover of middle-tier servers.</span>
  </a><a class="result" href="/boot2docker">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/773/6394678.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">boot2docker</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">92</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">boot2docker is a lightweight Linux distribution based on Tiny Core Linux made specifically to run Docker containers. It runs completely from RAM, weighs ~27MB and boots in ~5s (YMMV).</span>
  </a><a class="result" href="/airbrake">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/194/MCc1W3L8_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Airbrake</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">144</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Airbrake collects errors for your applications in all major languages and frameworks. We alert you to new errors and give you critical context, trends and details needed to find and fix errors fast.</span>
  </a><a class="result" href="/cmake">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2424/0UlUI_y1_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">CMake</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">301</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is used to control the software compilation process using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of the user's choice.</span>
  </a><a class="result" href="/laravel-homestead">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2001/74c5dd82a8b5540ab7dd4ce30fc0a2f6.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Laravel Homestead</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">29</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Laravel Homestead is an official, pre-packaged Vagrant "box" that provides you a wonderful development environment without requiring you to install PHP, HHVM, a web server, and any other server software on your local machine. Homestead runs on any Windows, Mac, or Linux system, and includes the Nginx web server, PHP 5.6, MySQL, Postgres, Redis, Memcached, and all of the other goodies you need to develop amazing Laravel applications.</span>
  </a><a class="result" href="/appium">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2855/0KVJyYNC_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Appium</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">57</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Appium is an open source test automation framework for use with native, hybrid, and mobile web apps. It drives iOS and Android apps using the WebDriver protocol. Appium is sponsored by Sauce Labs and a thriving community of open source developers.</span>
  </a><a class="result" href="/protractor">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1754/protractor-logo1.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Protractor</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">49</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Protractor is an end-to-end test framework for Angular and AngularJS applications. Protractor runs tests against your application running in a real browser, interacting with it as a user would.</span>
  </a><a class="result" href="/pm2">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2237/757747.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PM2</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">105</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Production process manager for Node.js apps with a built-in load balancer</span>
  </a><a class="result" href="/neovim">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/983/XDy-S1r6.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Neovim</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">16</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Neovim is a project that seeks to aggressively refactor Vim in order to: simplify maintenance and encourage contributions, split the work between multiple developers, enable the implementation of new/modern user interfaces without any modifications to the core source, and improve extensibility with a new plugin architecture.</span>
  </a><a class="result" href="/loggly">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/83/jy01f4p69n78p0nl4xou.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Loggly</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">114</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The world's most popular cloud-based log management service delivers application intelligence.</span>
  </a><a class="result" href="/stackdriver">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/734/lHYLxJV3_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Stackdriver</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">128</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Google Stackdriver provides powerful monitoring, logging, and diagnostics. It equips you with insight into the health, performance, and availability of cloud-powered applications, enabling you to find and fix issues faster. </span>
  </a><a class="result" href="/statuspage-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/279/sp-logo-blue-white-background.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">StatusPage.io</span>
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
    <span class="additional">The #1 status and incident communication tool. Use Statuspage to build trust with every incident. </span>
  </a><a class="result" href="/logentries">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/200/mNYt_Nwl.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Logentries</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">174</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Logentries makes machine-generated log data easily accessible to IT operations, development, and business analysis teams of all sizes. With the broadest platform support and an open API, Logentries brings the value of log-level data to any system, to any team member, and to a community of more than 25,000 worldwide users.</span>
  </a><a class="result" href="/capybara">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2595/capybara.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Capybara</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">169</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Capybara helps you test web applications by simulating how a real user would interact with your app. It is agnostic about the driver running your tests and comes with Rack::Test and Selenium support built in. WebKit is supported through an external gem.</span>
  </a><a class="result" href="/clion">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1445/icon_CLion.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">CLion</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">19</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Knowing your code through and through, CLion can take care of the routine while you focus on the important things. Boost your productivity with the keyboard-centric approach (Vim-emulation plugin is also available in plugin repository), full coding assistance, smart and relevant code completion, fast project navigation, intelligent intention actions, and reliable refactorings.</span>
  </a><a class="result" href="/appdynamics">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/105/C0eOfY-7.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AppDynamics</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">22</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AppDynamics develops application performance management (APM) solutions that deliver problem resolution for highly distributed applications through transaction flow monitoring and deep diagnostics.</span>
  </a><a class="result" href="/puppeteer">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7553/puppeteer.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Puppeteer</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">69</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Puppeteer is a Node library which provides a high-level API to control headless Chrome over the DevTools Protocol. It can also be configured to use full (non-headless) Chrome.</span>
  </a><a class="result" href="/buddy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4263/eIQHH23Q_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Buddy</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">38</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Git platform for web and software developers with Docker-based tools for Continuous Integration and Deployment.
</span>
  </a><a class="result" href="/apache-traffic-server">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6131/d2e0cf243d2a576d95fd70b82ddc79dc_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache Traffic Server</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">439</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a fast, scalable and extensible HTTP/1.1 and HTTP/2.0 compliant caching proxy server.Improve your response time, while reducing server load and bandwidth needs by caching and reusing frequently-requested web pages, images, and web ser</span>
  </a><a class="result" href="/phabricator">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/751/VE_3ve2I.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Phabricator</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">75</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Phabricator is a collection of open source web applications that help software companies build better software.</span>
  </a><a class="result" href="/uptime-robot">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/company/4322/G22d2Q6n_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Uptime Robot</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">105</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is all about helping you to keep your websites up. It monitors your websites every 5 minutes and alerts you if your sites are down.</span>
  </a><a class="result" href="/rubocop">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2643/rubocop.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">RuboCop</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">130</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">RuboCop is a Ruby static code analyzer. Out of the box it will enforce many of the guidelines outlined in the community Ruby Style Guide.</span>
  </a><a class="result" href="/statsd">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/932/codeascraft-twitter_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">StatsD</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">101</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">StatsD is a front-end proxy for the Graphite/Carbon metrics server, originally written by Etsy's Erik Kastner. StatsD is a network daemon that runs on the Node.js platform and listens for statistics, like counters and timers, sent over UDP and sends aggregates to one or more pluggable backend services (e.g., Graphite).</span>
  </a><a class="result" href="/concourse">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4949/jnsjSQcw_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Concourse</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">35</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Concourse's principles reduce the risk of switching to and from Concourse, by encouraging practices that decouple your project from your CI's little details, and keeping all configuration in declarative files that can be checked into version control. </span>
  </a><a class="result" href="/etcd">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1721/etcd.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">etcd</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">41</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">etcd is a distributed key value store that provides a reliable way to store data across a cluster of machines. It’s open-source and available on GitHub. etcd gracefully handles master elections during network partitions and will tolerate machine failure, including the master.</span>
  </a><a class="result" href="/bitrise">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2686/wFlFGsF3_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bitrise</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">76</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a Continous Integration and Delivery (CI/CD) Platform as a Service (PaaS) with a main focus on mobile app development (iOS, Android). You can automate the testing and deployment of your apps with just a few clicks. When you trigger a build a Virtual Machine is assigned to host your build and your defined Workflow (series of Steps scripts) will be executed, step by step.</span>
  </a><a class="result" href="/aws-codebuild">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6086/aws-codebuild.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS CodeBuild</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">62</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AWS CodeBuild is a fully managed build service that compiles source code, runs tests, and produces software packages that are ready to deploy. With CodeBuild, you don’t need to provision, manage, and scale your own build servers.</span>
  </a><a class="result" href="/tower">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1601/tower-dock-icon_transparent_2x.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Tower</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">45</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Use all of Git's powerful feature set - in a GUI that makes you more productive.</span>
  </a><a class="result" href="/go-cd">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2349/Z5QiBr7k_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GoCD</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">45</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">GoCD is an open source continuous delivery server created by ThoughtWorks. GoCD offers business a first-class build and deployment engine for complete control and visibility. </span>
  </a><a class="result" href="/iterm2">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3000/iTerm.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">iTerm2</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">36</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A replacement for Terminal and the successor to iTerm. It works on Macs with macOS 10.12 or newer. iTerm2 brings the terminal into the modern age with features you never knew you always wanted.</span>
  </a><a class="result" href="/aws-opswork">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/419/aws-opswork.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS OpsWorks</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">91</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Start from templates for common technologies like Ruby, Node.JS, PHP, and Java, or build your own using Chef recipes to install software packages and perform any task that you can script. AWS OpsWorks can scale your application using automatic load-based or time-based scaling and maintain the health of your application by detecting failed instances and replacing them. You have full control of deployments and automation of each component&nbsp;</span>
  </a><a class="result" href="/ngrok">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1309/ngrok.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ngrok</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">36</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">ngrok is a reverse proxy that creates a secure tunnel between from a public endpoint to a locally running web service. ngrok captures and analyzes all traffic over the tunnel for later inspection and replay.</span>
  </a><a class="result" href="/mercurial">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1047/mercurial.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mercurial</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">48</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Mercurial is dedicated to speed and efficiency with a sane user interface. It is written in Python. Mercurial's implementation and data structures are designed to be fast. You can generate diffs between revisions, or jump back in time within seconds.</span>
  </a><a class="result" href="/envoy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8416/Tfk-FtVd_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Envoy</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">47</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Originally built at Lyft, Envoy is a high performance C++ distributed proxy designed for single services and applications, as well as a communication bus and “universal data plane” designed for large microservice “service mesh” architectures.</span>
  </a><a class="result" href="/aws-cloudtrail">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/415/aws-cloudtrail.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS CloudTrail</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">67</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With CloudTrail, you can get a history of AWS API calls for your account, including API calls made via the AWS Management Console, AWS SDKs, command line tools, and higher-level AWS services (such as AWS CloudFormation). The AWS API call history produced by CloudTrail enables security analysis, resource change tracking, and compliance auditing. The recorded information includes the identity of the API caller, the time of the API call, the source IP address of the API caller, the request parameters, and the response elements returned by the AWS service.</span>
  </a><a class="result" href="/chai">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1725/chai.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Chai</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">151</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a BDD / TDD assertion library for node and the browser that can be delightfully paired with any javascript testing framework.  It has several interfaces that allow the developer to choose the most comfortable. The chain-capable BDD styles provide an expressive language &amp; readable style, while the TDD assert style provides a more classical feel.</span>
  </a><a class="result" href="/bazel">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2697/bazel.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bazel</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">20</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Bazel is a build tool that builds code quickly and reliably. It is used to build the majority of Google's software, and thus it has been designed to handle build problems present in Google's development environment.</span>
  </a><a class="result" href="/sensu">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1645/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sensu</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">48</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Sensu is the future-proof solution for multi-cloud monitoring at scale. The Sensu monitoring event pipeline empowers businesses to automate their monitoring workflows and gain deep visibility into their multi-cloud environments.</span>
  </a><a class="result" href="/wercker">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/897/S67KcxKE.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">wercker</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">62</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Wercker is a CI/CD developer automation platform designed for Microservices &amp; Container Architecture.</span>
  </a><a class="result" href="/google-cloud-container-builder">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6636/container-engine.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Cloud Container Builder</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">15</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Run your container image builds in a fast, consistent, and reliable environment on Google Cloud Platform. Build in any language and package your build artifacts into Docker containers for deployment. </span>
  </a><a class="result" href="/codemirror">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2490/E_fCaAi6.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">CodeMirror</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">158</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">CodeMirror is a JavaScript component that provides a code editor in the browser. When a mode is available for the language you are coding in, it will color your code, and optionally help with indentation.</span>
  </a><a class="result" href="/gogs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1365/ZSXhTUMn_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gogs</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">19</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The goal of this project is to make the easiest, fastest and most painless way to set up a self-hosted Git service. With Go, this can be done in independent binary distribution across ALL platforms that Go supports, including Linux, Mac OS X, and Windows.
</span>
  </a><a class="result" href="/sumo-logic">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/370/Qz_ocsrM.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sumo Logic</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">76</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Cloud-based machine data analytics platform that enables companies to proactively identify availability and performance issues in their infrastructure, improve their security posture and enhance application rollouts. Companies using Sumo Logic reduce their mean-time-to-resolution by 50% and can save hundreds of thousands of dollars, annually.  Customers include Netflix, Medallia, Orange, and GoGo Inflight.  </span>
  </a><a class="result" href="/splunk-cloud">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/287/facebook-180-180.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Splunk Cloud</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">15</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">If you're looking for all the benefits of Splunk® Enterprise with all the benefits of software-as-a-service, then look no further. Splunk Cloud is backed by a 100% uptime SLA, scales to over 10TB/day, and offers a highly secure environment.</span>
  </a><a class="result" href="/netdata">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5766/logo_green_fill.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">NetData</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">16</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Netdata is distributed, real-time, performance and health monitoring for systems and applications. It is a highly optimized monitoring agent you install on all your systems and containers.</span>
  </a><a class="result" href="/spacemacs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3261/HUlKNR_N.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Spacemacs</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Since version 0.101.0 and later Spacemacs totally abolishes the frontiers between Vim and Emacs. The user can now choose his/her preferred editing style and enjoy all the Spacemacs features.

Even better, it is possible to dynamically switch between the two styles seamlessly which makes it possible for programmers with different styles to do seat pair programming using the same editor.</span>
  </a><a class="result" href="/visual-studio-live-share">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7894/jEKFRPKV_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Visual Studio Live Share</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">8</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">When you start a live share session in Visual Studio 2017 or Visual Studio Code, your teammates get instant and secure access to your code in their own tool – no need to clone, copy, or configure anything.</span>
  </a><a class="result" href="/nomad">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3695/nomad.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Nomad</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">44</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Nomad is a cluster manager, designed for both long lived services and short lived batch processing workloads. Developers use a declarative job specification to submit work, and Nomad ensures constraints are satisfied and resource utilization is optimized by efficient task packing. Nomad supports all major operating systems and virtualized, containerized, or standalone applications.
</span>
  </a><a class="result" href="/jenkins-x">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8884/5Lk6ASPJ_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Jenkins X</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">14</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Jenkins X is a CI/CD solution for modern cloud applications on Kubernetes</span>
  </a><a class="result" href="/jfrog-artifactory">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4711/jfrog-artifactory-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">JFrog Artifactory</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">47</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It integrates with your existing ecosystem supporting end-to-end binary management that overcomes the complexity of working with different software package management systems, and provides consistency to your CI/CD workflow.</span>
  </a><a class="result" href="/hockeyapp">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/96/436e2f6e2e5b488a3ed636b6f37adb98.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">HockeyApp</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">66</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">HockeyApp is the best way to collect live crash reports, get feedback from your users, distribute your betas, and analyze your test coverage.</span>
  </a><a class="result" href="/buildkite">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/577/icon-square-no-padding.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Buildkite</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">71</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">CI and build automation tool that combines the power of your own build infrastructure with the convenience of a managed, centralized web UI. Used by Shopify, Basecamp, Digital Ocean, Venmo, Cochlear, Bugsnag and more.</span>
  </a><a class="result" href="/bitbucket-pipeline">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7452/35O2KIRX_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bitbucket Pipelines</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">80</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an Integrated continuous integration and continuous deployment for Bitbucket Cloud that's trivial to set up, automating your code from test to production. Our mission is to enable all teams to ship software faster by driving the practice of continuous delivery. </span>
  </a><a class="result" href="/jaeger">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8123/28545596.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Jaeger</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">44</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Jaeger, a Distributed Tracing System</span>
  </a><a class="result" href="/jetbrains-rider">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7410/lh1l265w_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">JetBrains Rider</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">32</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It supports .NET Framework, the new cross-platform .NET Core, and Mono based projects. It lets you develop a wide range of applications including .NET desktop applications, services and libraries, Unity games, Xamarin apps, ASP.NET, and ASP.NET Core web applications.</span>
  </a><a class="result" href="/spinnaker">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7674/7634182.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Spinnaker</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">35</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Created at Netflix, it has been battle-tested in production by hundreds of teams over millions of deployments. It combines a powerful and flexible pipeline management system with integrations to the major cloud providers.</span>
  </a><a class="result" href="/gitea">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6378/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gitea</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">22</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Gitea is a community managed lightweight code hosting solution written in Go. It published under the MIT license.</span>
  </a><a class="result" href="/semaphore">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/324/S0nf9Rux_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Semaphore</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">59</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Semaphore is the fastest continuous integration and delivery (CI/CD) platform on the market, powering the world’s best engineering teams.</span>
  </a><a class="result" href="/azure-application-insights">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6336/azure-application-insignts.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Azure Application Insights</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">34</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is use to monitor your live web application. It will automatically detect performance anomalies. It includes powerful analytics tools to help you diagnose issues and to understand what users actually do with your app.</span>
  </a><a class="result" href="/opsgenie">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1185/_drviLrV_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OpsGenie</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">72</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">OpsGenie is a cloud-based service for dev &amp; ops teams, providing reliable alerts, on-call schedule management, and escalations. OpsGenie integrates with monitoring tools &amp; services and ensures that the right people are at the right time.</span>
  </a><a class="result" href="/azure-pipelines">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/10164/528389819366_e7a0672f0480b3e98d21_512.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Azure Pipelines</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">30</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Fast builds with parallel jobs and test execution. Use container jobs to create consistent and reliable builds with the exact tools you need. Create new containers with ease and push them to any registry.</span>
  </a><a class="result" href="/wakatime">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2742/oTO48khk.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">WakaTime</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">22</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Quantify your coding - open source plugins for automatic time tracking &amp; insights into your programming.</span>
  </a><a class="result" href="/ant">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/976/ant.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache Ant</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">41</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Ant is a Java-based build tool. In theory, it is kind of like Make, without Make's wrinkles and with the full portability of pure Java code.</span>
  </a><a class="result" href="/mockito">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2021/4y634TJm_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mockito</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">62</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a mocking framework that tastes really good. It lets you write beautiful tests with a clean &amp; simple API. It doesn’t give you hangover because the tests are very readable and they produce clean verification errors. </span>
  </a><a class="result" href="/raygun">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/192/jTDjfbiS_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Raygun</span>
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
    <span class="additional">Raygun gives you a window into how users are really experiencing your software applications. Detect, diagnose and resolve issues that are affecting end users with greater speed and accuracy.</span>
  </a><a class="result" href="/component">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/848/b5afc399fabed86ab0580f68f8b9b553.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Component</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">29</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Component's philosophy is the UNIX philosophy of the web - to create a platform for small, reusable components that consist of JS, CSS, HTML, images, fonts, etc. With its well-defined specs, using Component means not worrying about most frontend problems such as package management, publishing components to a registry, or creating a custom build process for every single app.</span>
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
data.to_csv('C:/Users/i9i91/OneDrive/바탕 화면/github 저장내용/portfolio.io/크롤링3.csv')  




