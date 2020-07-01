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
<a class="result" href="/slack">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/675/RNiSRYOF_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Slack</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7497</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Imagine all your team communication in one place, instantly searchable, available wherever you go. That’s Slack. All your messages. All your files. And everything from Twitter, Dropbox, Google Docs, Asana, Trello, GitHub and dozens of other services. All together.</span>
  </a><a class="result" href="/wordpress">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/250/logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">WordPress</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">48302</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The core software is built by hundreds of community volunteers, and when you’re ready for more there are thousands of plugins and themes available to transform your site into almost anything you can imagine. Over 60 million people have chosen WordPress to power the place on the web they call “home” — we’d love you to join the family.</span>
  </a><a class="result" href="/gmail">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3167/_K34MGL8_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gmail</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">37480</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">An easy to use email app that saves you time and keeps your messages safe. Get your messages instantly via push notifications, read and respond online &amp; offline, and find any message quickly.</span>
  </a><a class="result" href="/font-awesome">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3244/1_Mr1Fy00XjPGNf1Kkp_hWtw_2x.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Font Awesome</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">37079</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">You can get vector icons and social logos on your website with it. It is a font that's made up of symbols, icons, or pictograms that you can use in a webpage, just like a font.</span>
  </a><a class="result" href="/jira">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/154/Qifq4jpS_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Jira</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3497</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Jira's secret sauce is the way it simplifies the complexities of software development into manageable units of work. 
Jira comes out-of-the-box with everything agile teams need to ship value to customers faster.</span>
  </a><a class="result" href="/trello">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/109/-CvHThPk_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Trello</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3210</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Trello is a collaboration tool that organizes your projects into boards. In one glance, Trello tells you what's being worked on, who's working on what, and where something is in a process.</span>
  </a><a class="result" href="/g-suite">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/247/oYkAxyQM_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">G Suite</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12677</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">An integrated suite of secure, cloud-native collaboration and productivity apps. It includes Gmail, Docs, Drive, Calendar, Meet and more.</span>
  </a><a class="result" href="/mailchimp">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/47/69XlPqVT.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mailchimp</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7210</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">MailChimp helps you design email newsletters, share them on social networks, integrate with services you already use, and track your results. It's like your own personal publishing platform.</span>
  </a><a class="result" href="/confluence">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/769/5_z16TbH_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Confluence</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1953</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Capture the knowledge that's too often lost in email inboxes and shared network drives in Confluence instead – where it's easy to find, use, and update.</span>
  </a><a class="result" href="/google-adsense">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5137/xvWejEyc_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google AdSense</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">14492</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a program run by Google through which website publishers in the Google Network of content sites serve text, images, video, or interactive media advertisements that are targeted to the site content and audience. </span>
  </a><a class="result" href="/skype">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/340/skype.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Skype</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1108</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Skype’s text, voice and video make it simple to share experiences with the people that matter to you, wherever they are.</span>
  </a><a class="result" href="/drupal">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1226/H9IAAYru_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Drupal</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6276</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Drupal is an open source content management platform powering millions of websites and applications. It’s built, used, and supported by an active and diverse community of people around the world.</span>
  </a><a class="result" href="/invision">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/165/r9uL4jWU.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">InVision</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1411</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">InVision lets you create stunningly realistic interactive wireframes and prototypes without compromising your creative vision.</span>
  </a><a class="result" href="/asana">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/108/asana.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Asana</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">955</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Asana is the easiest way for teams to track their work. From tasks and projects to conversations and dashboards, Asana enables teams to move work from start to finish--and get results. Available at asana.com and on iOS &amp; Android.
</span>
  </a><a class="result" href="/hubspot">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/256/9Q0oQwl2_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">HubSpot</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3686</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Attract, convert, close and delight customers with HubSpot’s complete set of marketing tools. HubSpot all-in-one marketing software helps more than 12,000 companies in 56 countries attract leads and convert them into customers. </span>
  </a><a class="result" href="/zendesk">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/70/ObVtJEgP_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zendesk</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2196</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Zendesk provides an integrated on-demand helpdesk - customer support portal solution based on the latest Web 2.0 technologies and design philosophies.</span>
  </a><a class="result" href="/intercom">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/257/qmwr6vjg_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Intercom</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2923</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Intercom is a customer communication platform with a suite of integrated products for every team—including sales, marketing, product, and support. Have targeted communication with customers on your website, inside  apps, and by email.</span>
  </a><a class="result" href="/salesforce-sales-cloud">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/35/lGZFUPOW.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Salesforce Sales Cloud</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">849</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The Sales Cloud puts everything you need at your fingertips—available anywhere. From Social accounts and contacts to Mobile, Chatter, and Analytics, collaboration across your global organization and getting deals done faster is not only possible, it's easy.</span>
  </a><a class="result" href="/adroll">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/149/f75dfcf3cf533e77fa92148d9183397c.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AdRoll</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2521</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AdRoll is the most effective retargeting platform in the world. We’re trusted by more companies than anyone else. AdRoll takes just minutes to setup.</span>
  </a><a class="result" href="/acquia">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8246/uXDAUlXc_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Acquia</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3161</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The leader in enterprise Drupal solutions providing a powerful cloud-native platform to build, operate, and optimize your digital experience. It provide enterprise products, services, and technical support for the open-source web content management platform Drupal.</span>
  </a><a class="result" href="/hipchat">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/144/R2NV13gL.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">HipChat</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">379</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">HipChat is a hosted private chat service for your company or team. Invite colleagues to share ideas and files in persistent group chat rooms. Get your team off AIM, Google Talk, and Skype — HipChat was built for business.</span>
  </a><a class="result" href="/sketch">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4561/c07jH7QS.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sketch</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">534</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Easily create complex shapes with our state-of-the-art vector boolean operations and take advantage of our extensive layer styles.</span>
  </a><a class="result" href="/adobe-photoshop">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3176/lxVcZyci.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Adobe Photoshop</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">211</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the best in the world of graphic design and image processing software that will realize any of your ideas. Create and enhance photos, illustrations and 3D graphic objects.</span>
  </a><a class="result" href="/zoho-mail">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3616/FRau1Ij3_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zoho Mail</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2101</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a secure and reliable business email solution tailor-made for your organization's communication needs. With enhanced collaboration features, it's not just an inbox—it's more.</span>
  </a><a class="result" href="/marketo">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/56/4uY7BObm.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Marketo</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1420</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Marketing automation, social campaigns, inbound marketing, sales apps, ROI reporting - all in one place.</span>
  </a><a class="result" href="/zoom">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6083/uGzVfgaE.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zoom</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">209</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Zoom unifies cloud video conferencing, simple online meetings, and cross platform group chat into one easy-to-use platform. Our solution offers the best video, audio, and screen-sharing experience across Zoom Rooms, Windows, Mac, iOS, Android, and H.323/SIP room systems.</span>
  </a><a class="result" href="/zapier">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/286/0bd8e9aaccec949490082ad22c7ee60f.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zapier</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">343</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Zapier is for busy people who know their time is better spent selling, marketing, or coding. Instead of wasting valuable time coming up with complicated systems - you can use Zapier to automate the web services you and your team are already using on a daily basis.</span>
  </a><a class="result" href="/joomla">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1227/SYUsgebu_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Joomla!</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1182</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Joomla is a simple and powerful web server application and it requires a server with PHP and either MySQL, PostgreSQL, or SQL Server to run it.</span>
  </a><a class="result" href="/microsoft-teams">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5989/teams.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Microsoft Teams</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">177</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">See content and chat history anytime, including team chats with Skype that are visible to the whole team. Private group chats are available for smaller group conversations.</span>
  </a><a class="result" href="/figma">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7007/MFYQOphW_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Figma</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">255</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Figma is the first interface design tool with real-time collaboration. It keeps everyone on the same page. Focus on the work instead of fighting your tools.</span>
  </a><a class="result" href="/balsamiq">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/141/LJf-7p3B.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Balsamiq</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">253</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Balsamiq Mockups is a web tool that allows users to mock up different designs and ideas quickly and easily. Balsamic Mockups is similar to drawing mockups, but it is digital</span>
  </a><a class="result" href="/adobe-illustrator">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3175/adobe-illustrator.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Adobe Illustrator</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">164</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The industry-standard vector graphics app lets you create logos, icons, sketches, typography, and complex illustrations for print, web, interactive, video, and mobile.</span>
  </a><a class="result" href="/discord">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4418/gT8yKJa7.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Discord</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">116</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Discord is a modern free voice &amp; text chat app for groups of gamers. Our resilient Erlang backend running on the cloud has built in DDoS protection with automatic server failover.</span>
  </a><a class="result" href="/medium">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1225/57136-4b1a5b74c7fc047afba480ca3d0bdb80-medium_jpg.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Medium</span>
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
    <span class="additional">Medium is a different kind of place on the internet. A place where the measure of success isn’t views, but viewpoints. Where the quality of the idea matters, not the author’s qualifications. A place where conversation pushes ideas forward.</span>
  </a><a class="result" href="/pivotal-tracker">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1/422314579c5a2b89852d2ba6432d7716.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Pivotal Tracker</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">253</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a collaborative, lightweight agile project management tool, brought to you by the experts in agile software development.</span>
  </a><a class="result" href="/zeplin">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3457/SNbLveBx.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zeplin</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">306</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Collaboration app for designers &amp; developers. Supports Sketch and Photoshop (on beta!).</span>
  </a><a class="result" href="/google-sheets">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1100/google-sheets.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Sheets</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">145</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Access, create, and edit your spreadsheets wherever you go—from your phone, tablet, or computer.</span>
  </a><a class="result" href="/basecamp">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/110/X-gfZudw_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Basecamp</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">168</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Basecamp is a project management and group collaboration tool. The tool includes features for schedules, tasks, files, and messages.</span>
  </a><a class="result" href="/notion-so">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6758/cbCR7w5R_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">notion.so</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">191</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A new tool that blends your everyday work apps into one. It's a unified and collaborative workspace for you and your team</span>
  </a><a class="result" href="/contentful">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/672/Contentful_white_logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Contentful</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">311</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Contentful enables teams to unify content in a single hub, structure it for use in any digital channel, and integrate seamlessly with hundreds of other tools through open APIs and a leading app framework.</span>
  </a><a class="result" href="/tawk-to">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3949/thi6k5bh_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">tawk.to</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">831</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a live chat support &amp; messaging application that focuses on successful communication between businesses and their customers.</span>
  </a><a class="result" href="/microsoft-office-365">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4167/KkVyIqPN_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Microsoft Office 365</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">188</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Collaborate for free with online versions of Microsoft Word, PowerPoint, Excel, and OneNote. Save documents, spreadsheets, and presentations online, in OneDrive. Share them with others and work together at the same time.</span>
  </a><a class="result" href="/redmine">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1186/redmine-logo-twitter_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Redmine</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">136</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Redmine is a flexible project management web application. Written using the Ruby on Rails framework, it is cross-platform and cross-database. </span>
  </a><a class="result" href="/adobe-experience-manager">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4343/8ei_UuLc_200x200.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Adobe Experience Manager</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">725</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a Web Content Management System that allows companies to manage their web content (Web pages, digital assets, forms, etc) and also create digital experiences with this content on any platform web, mobile or IoT.</span>
  </a><a class="result" href="/airtable">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1512/logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Airtable</span>
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
    <span class="additional">Working with Airtable is as fast and easy as editing a spreadsheet. But only Airtable is backed by the power of a full database, giving you rich features far beyond what a spreadsheet can offer.</span>
  </a><a class="result" href="/livechat">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/119/yGTwda9h_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">LiveChat</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">690</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">LiveChat provides a live chat application with help desk and web analytics functionalities, allowing online businesses to communicate with visitors in real time.</span>
  </a><a class="result" href="/ghost">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1228/XRKixLnT_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Ghost</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">200</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Ghost is a platform dedicated to one thing: Publishing. It's beautifully designed, completely customisable and completely Open Source. Ghost allows you to write and publish your own blog, giving you the tools to make it easy and even fun to do.</span>
  </a><a class="result" href="/mattermost">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3254/xiE1dr2s_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mattermost</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">74</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Mattermost is modern communication from behind your firewall. </span>
  </a><a class="result" href="/rocketchat">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3124/14EIApTi_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">RocketChat</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">58</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Rocket.Chat is a Web Chat Server, developed in JavaScript, using the Meteor fullstack framework.

It is a great solution for communities and companies wanting to privately host their own chat service or for developers looking forward to build and evolve their own chat platforms.</span>
  </a><a class="result" href="/buffer">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/825/hnc3q-7x.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Buffer</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">139</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Buffer helps you manage multiple social media accounts at once. Quickly schedule content from anywhere on the web, collaborate with team members, and analyze rich statistics on how your posts perform.</span>
  </a><a class="result" href="/telegram">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3940/m6BFtJQW_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Telegram </span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">45</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Users can send messages and exchange photos, videos, stickers, audio and files of any type. It provides instant messaging, simple, fast, secure and synced across all your devices. </span>
  </a><a class="result" href="/olark">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/117/twitter-pic-olark.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Olark</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">360</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Olark is a lightweight tool to chat with visitors to your website using your existing instant messaging client. Visitors to your website appear as buddies on your Buddy list, their messages to you appear as IMs.</span>
  </a><a class="result" href="/zopim">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/120/def00f4817221e65844412e1971e44fc.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zopim</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">342</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Zopim is focused on serving the needs of web users that hasn’t been met by other chat solutions: the need for usability, convenience and simplicity of design</span>
  </a><a class="result" href="/jitsi">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9412/F0VxeYZj_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Jitsi</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Jitsi is a set of open-source projects that allows you to easily build and deploy secure videoconferencing solutions. At the heart of Jitsi are Jitsi Videobridge and Jitsi Meet, which let you have conferences on the internet, while other projects in the community enable other features such as audio, dial-in, recording, and simulcasting.</span>
  </a><a class="result" href="/freshdesk">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/72/d0xmceuw_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">FreshDesk</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">213</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Freshdesk is an on demand customer support software that works across multiple support channels.</span>
  </a><a class="result" href="/google-meet">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8683/246x0w.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Meet</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">35</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the business-oriented version of Google's Hangouts platform and is suitable for businesses of all sizes. It allows users to dial in phone numbers to access meetings, thus enabling users with slow internet connection to call in.</span>
  </a><a class="result" href="/blogger">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/251/blogger_hires.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Blogger</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">448</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Since Blogger was launched in 1999, blogs have reshaped the web, impacted politics, shaken up journalism, and enabled millions of people to have a voice and connect with others.</span>
  </a><a class="result" href="/unbounce">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/78/GEI0oMKZ.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Unbounce</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">417</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Unbounce is a self-serve hosted service that provides marketers doing paid search, banner ads, email or social media marketing, the easiest way to create, publish &amp; test promotion specific landing pages without the need for IT or developers.</span>
  </a><a class="result" href="/uservoice">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/122/twitter_avatar_UserVoice.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">UserVoice</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">254</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">UserVoice creates simple customer engagement tools that help companies understand and interact with their customers more positively and build customer relationships that last.</span>
  </a><a class="result" href="/wix">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4656/tvOXJHAG_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Wix</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">352</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Creating your stunning website for free is easier
than ever. No tech skills needed. Just pick a template,
change anything you want, add your images, videos,
text and more to get online instantly.</span>
  </a><a class="result" href="/netlify-cms">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7613/YIgPht1s_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Netlify CMS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">13</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is built as a single-page React app. You can create custom-styled previews, UI widgets, and editor plugins or add backends to support different Git platform APIs.</span>
  </a><a class="result" href="/gitter">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/715/1uZZ-5YI.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gitter</span>
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
    <span class="additional">Free chat rooms for your public repositories. 
A bit like IRC only smarter. Chats for private repositories as well as organisations.</span>
  </a><a class="result" href="/xenforo">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6119/xf_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">XenForo</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">521</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a commercial Internet forum software package written in the PHP programming language.</span>
  </a><a class="result" href="/ifttt">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1085/TIT71OZq.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">IFTTT</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">40</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Create powerful connections with one simple statement: if this then that. For example: "Backup my contacts to a Google Spreadsheet"</span>
  </a><a class="result" href="/lastpass">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1286/Zhbxv1nv_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">LastPass</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">55</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">LastPass Enterprise offers your employees and admins a single, unified experience that combines the power of SAML SSO coupled with enterprise-class password vaulting. LastPass is your first line of defense in the battle to protect your digital assets from the significant risks associated with employee password re-use and phishing.</span>
  </a><a class="result" href="/tumblr">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/252/d5mgh_8L.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Tumblr</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">131</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Tumblr is a feature rich and free blog hosting platform offering professional and fully customizable templates, bookmarklets, photos, mobile apps, and social network. The site now ranks as the 11th-largest in terms of traffic, according to Quantcast, with 170 million monthly visitors globally.</span>
  </a><a class="result" href="/zulip">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3449/672c2cf6c1404b1e17459153e726dca4.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zulip</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">11</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Zulip is powerful, open source team chat that combines the immediacy of real-time chat with the productivity benefits of threaded conversations.

Zulip allows busy managers and others in meetings all day to participate in their teams chats.</span>
  </a><a class="result" href="/hubot">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1519/hubot.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Hubot</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">69</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Hubot is a chat bot, modeled after GitHub's Campfire bot, hubot. He's pretty cool. He's extendable with old community scripts, or new community org and your own custom scripts, and can work on many different chat services.</span>
  </a><a class="result" href="/zenhub">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1589/6d14af3a-bbab-11e5-9206-d68fba762c54.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ZenHub</span>
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
    <span class="additional">ZenHub is a lightweight browser extension that adds a powerful set of features directly into GitHub's UI. </span>
  </a><a class="result" href="/help-scout">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/267/bccc66f7e2cdbbb15da06d5f12c5b082.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Help Scout</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">255</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With best in-class-reporting, an integrated knowledge base, 50+ integrations and a robust API, Help Scout lets your team focus on what really matters: your customers.</span>
  </a><a class="result" href="/superset">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4908/superset2.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Superset</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">30</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Superset's main goal is to make it easy to slice, dice and visualize data. It empowers users to perform analytics at the speed of thought.</span>
  </a><a class="result" href="/okta">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1285/ieibivdE.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Okta</span>
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
    <span class="additional">Connect all your apps in days, not months, with instant access to thousands of pre-built integrations - even add apps to the network yourself. Integrations are easy to set up, constantly monitored, proactively repaired and handle authentication and provisioning.</span>
  </a><a class="result" href="/1password">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7122/jPhaQEQv_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">1Password</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">58</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">1Password is the best password manager and secure wallet for Mac, Windows, iOS, and Android. Securely generate, store, and fill passwords and much more.</span>
  </a><a class="result" href="/expressionengine">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5141/0dRRApei_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ExpressionEngine</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">438</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a flexible, feature-rich, free open-source content management platform that empowers hundreds of thousands of individuals and organizations around the world to easily manage their web site.</span>
  </a><a class="result" href="/opencart">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5990/Z2X4a21N_400x400.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OpenCart</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">347</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an online store management system. It is PHP-based, using a MySQL database and HTML components. Support is provided for different languages and currencies. It is freely available under the GNU General Public License.</span>
  </a><a class="result" href="/firefox">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8705/768px-Firefox_Logo__2017.svg.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Firefox</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">44</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A free and open source web browser developed by The Mozilla Foundation and its subsidiary, Mozilla Corporation. Firefox is available for Microsoft Windows, macOS, Linux, BSD, and more.</span>
  </a><a class="result" href="/customer-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/255/preview.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Customer.io</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">208</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Send segmented newsletters without bugging developers. Change transactional emails without re-deploying your app. Create lifecycle emails to activate more customers</span>
  </a><a class="result" href="/logrocket">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6063/logo_bg.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">LogRocket</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">93</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">LogRocket helps product teams build better experiences for their users. By recording videos of user sessions along with logs and network data, LogRocket surfaces UX problems and reveals the root cause of every bug.</span>
  </a><a class="result" href="/pipedrive">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2733/7NdrIqpR_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Pipedrive</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">95</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Pipeline tool for active dealmakers. Get super-organized. Close deals in less time. Built by active salespeople and serious web app developers.</span>
  </a><a class="result" href="/fullstory">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3365/gyA5IJZO_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">FullStory</span>
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
    <span class="additional">Our tiny script unlocks pixel-perfect session playback, automatic insights, funnel analytics, and robust search and segmentation – empowering everyone in your organization to help build the best online experience for your customers.</span>
  </a><a class="result" href="/webrtc">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2262/xDgK1jYK_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">WebRTC</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">25</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a free, open project that enables web browsers with Real-Time Communications (RTC) capabilities via simple JavaScript APIs. The WebRTC components have been optimized to best serve this purpose.</span>
  </a><a class="result" href="/typeform">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2757/HQwTKlIn_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Typeform</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">67</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Build beautiful and engaging next-generation online forms, surveys, quizzes, landing pages, and much more with Typeform</span>
  </a><a class="result" href="/clickup">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9192/dSV8FSuF_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ClickUp</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">36</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Users can assign comments and tasks to specific team members or groups of team members. Comments and tasks can be marked as resolved or in progress, or users can create custom statuses.</span>
  </a><a class="result" href="/marvel">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/660/MK1nK9oz.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Marvel</span>
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
    <span class="additional">A super simple tool that turns any image (including PSDs) or sketch into interactive prototypes for any device.

Powered by Dropbox.</span>
  </a><a class="result" href="/freshchat">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9539/nSSKgPzx_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Freshchat</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">301</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Freshchat is a modern messaging software built for teams who want to ace customer conversations—marketing, sales, or support.</span>
  </a><a class="result" href="/waffle-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/780/dVIEyFe8.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">waffle.io</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">50</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Track priority and rank for your GitHub issues across multiple repositories. Automatically see issues moved across a board for you, when you open pull requests or create branches. </span>
  </a><a class="result" href="/google-ads">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2408/UimQskO__400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Ads</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">65</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">An online advertising solution that businesses use to promote their products and services on Google Search, YouTube and other sites across the web. It also allows advertisers to choose specific goals for their ads, like driving phone calls or website visits.</span>
  </a><a class="result" href="/webex">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/162/VKrmoYeC_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Webex</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">11</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Collaborate with colleagues across your organization, or halfway across the planet. Meet online and share files, information, and expertise. Collaborate from wherever you are with WebEx mobile apps for IPhone, iPad, Android, or Blackberry. If you can get online, you can work together.</span>
  </a><a class="result" href="/docusign">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/160/hIR6V9z0_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">DocuSign</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">35</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">DocuSign automates manual, paper-based processes allowing you to manage all aspects of documented business transactions, including identity management, authentication, digital signature, forms/data collection, collaboration, workflow automation and storage. </span>
  </a><a class="result" href="/zoho-crm">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/32/-VpX0bb7_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zoho CRM</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">46</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Online CRM software for managing your sales, marketing, customer support, and inventory in a single system</span>
  </a><a class="result" href="/monday">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9761/monday_logo_icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">monday.com</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">26</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A tool that simplifies the way teams work together - Manage workload, track projects, move work forward, communicate with people - Adopt a management tool that people actually love to use, one that's fast, and easy to use.</span>
  </a><a class="result" href="/facebook-ads">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5144/X4G0h2LY_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Facebook Ads</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">35</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is targeted to users based on their location, demographic, and profile information. Many of these options are only available</span>
  </a><a class="result" href="/campaign-monitor">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/48/GYLX84mG_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Campaign Monitor</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">59</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Campaign Monitor makes it easy to attract new subscribers, send them beautiful email newsletters and see stunning reports on the results.</span>
  </a><a class="result" href="/clubhouse">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3393/cloubhouse-icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Clubhouse</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">65</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Clubhouse combines a simple, modern UI with enterprise-grade tools, allowing technology companies to plan and manage their projects effectively, visualize progress across the organization, and define deadlines and milestones based upon data and predictive modeling.</span>
  </a><a class="result" href="/drawio">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2450/Hh-vWsQ0_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">drawio</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">34</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a free online diagram software for making flowcharts, process diagrams, org charts, UML, ER and network diagrams. It is an open platform where you can create and share diagrams. It’s integrated with the tools you already use.</span>
  </a><a class="result" href="/evernote">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1664/Msdwofz8_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Evernote</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">13</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Take notes to a new level with Evernote, the productivity app that keeps your projects, ideas, and inspiration handy across all your digital devices. It helps you capture and prioritize ideas, projects, and to-do lists, so nothing falls through the cracks.</span>
  </a><a class="result" href="/xero">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1610/_LiT6IcT.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Xero</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">57</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Inventory, invoicing, time tracking, expenses, and hundreds of other apps all seamlessly integrate with Xero to save your business precious time and money.</span>
  </a><a class="result" href="/octobercms">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2395/orange-fg-white-bg.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OctoberCMS</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">18</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">October is a Content Management System (CMS) and web platform whose sole purpose is to make your development workflow simple again. We feel building websites has become a convoluted and confusing process that leaves developers unsatisfied, we want to turn you around to the simpler side and get back to basics.</span>
  </a><a class="result" href="/toggl">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1604/017e79a95ca24d46f1794e9b2d6209ed_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Toggl</span>
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
    <span class="additional">Toggl is an online time-tracking tool. It is popular with freelancers, groups, and small companies all over the world, mostly in US, Canada and UK.</span>
  </a><a class="result" href="/azure-active-directory">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6346/azure-active-directory.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Azure Active Directory</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">34</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a comprehensive identity and access management solution that gives you a robust set of capabilities to manage users and groups. You can get the reliability and scalability you need with identity services that work with your on-premises, cloud, or hybrid environment.</span>
  </a><a class="result" href="/craft">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1235/PhuPlrl7_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Craft</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">56</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Craft is a content management system (CMS) that’s laser-focused on doing one thing really, really well: managing content. </span>
  </a><a class="result" href="/lighthouse">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/183/lighthouse_fluid_icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Lighthouse</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">14</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Collaborate effortlessly on projects. Whether you’re a team of 5 or studio of 50, Lighthouse will help you keep track of your project development with ease. We give you all the tools you need to organize your tickets – custom states, a powerful tagging system, an advanced search, saved searches (we call them ticket bins), and a mass editing tool.</span>
  </a><a class="result" href="/google-docs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4575/google-docs.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Docs</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">40</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a word processor included as part of a free, web-based software office suite offered by Google. It brings your documents to life with smart editing and styling tools to help you easily format text and paragraphs.</span>
  </a><a class="result" href="/prismic-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/673/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">prismic.io</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">33</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Prismic is a Content Management System, a tool for editing online content, also known as a headless CMS, an API CMS, a content platform, a disruptive content-as-a-service digital experience.</span>
  </a><a class="result" href="/appear-in">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2300/Y3UHc1cn.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">appear.in</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">39</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Create a video room. Share the link. Appear together. Built with WebRTC &amp; AngularJS.</span>
  </a><a class="result" href="/aha">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/802/ed282c37de4d79f873c7e9b6ea7da342.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Aha!</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">39</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Set product strategy, visualize and share roadmaps, and articulate features so your product development teams can build what matters. </span>
  </a><a class="result" href="/adobe-lightroom">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7010/images.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Adobe Lightroom</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a cloud-based service for people who love photography, it gives you everything you need to edit, organize, store, and share your photos across desktop, mobile, and web.</span>
  </a><a class="result" href="/flowdock">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/547/-vh2vDWG_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Flowdock</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">46</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Flowdock is a web-based team chat service that integrates with your tools to provide a window into your team's activities. With the team inbox, everyone on your team can stay up to date. Stay connected with Flowdock's iOS and Android apps.</span>
  </a><a class="result" href="/qualaroo">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/155/24nfg6mk8tlrywrfyg26.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Qualaroo</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">128</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Once you implement the Qualaroo code (it generally only takes a couple minutes), you can easily target a survey question or two as users are making decisions on your website. Your customers will see it slide up from the bottom right-hand corner of your site.</span>
  </a><a class="result" href="/activecampaign">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/371/qZNppe_4_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ActiveCampaign</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">25</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Recognized as the leader in the marketing and sales automation for small businesses, ActiveCampaign helps over 70k growing businesses meaningfully connect and engage with their customers with personalized, intelligence-driven messages. </span>
  </a><a class="result" href="/harvest">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/234/053rrzypvrxxrrtwfl3t.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Harvest</span>
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
    <span class="additional">Time tracking is simple and lightning fast with Harvest. Set up takes seconds, and there's nothing to install. We've simplified the timesheet and timesheets approval process so you can stay focused on work.</span>
  </a><a class="result" href="/drift">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5214/FQQPh3uG.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Drift</span>
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
    <span class="additional">Drift is a messaging app that makes it easy for businesses to talk to their website visitors and customers in real-time, from anywhere.</span>
  </a><a class="result" href="/jira-service-desk">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1860/oIyuo8uz_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Jira Service Desk</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">29</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It lets you receive, track, manage and resolve requests from your team's customers. It is built for IT, support, and internal business teams, it empowers teams to track, prioritize, and resolve service requests, all in one place.</span>
  </a><a class="result" href="/builder">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/11244/builder.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Builder</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the first and only headless CMS with full drag and drop editing. It supports many frameworks like Angular, Vue, React, Preact etc. </span>
  </a><a class="result" href="/calendly">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1310/UljSkwcI.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Calendly</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">28</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Spend 1 minute telling Calendly your availability preferences. Share your personal Calendly page with clients, colleagues, students, etc. Invitees visit your Calendly page to pick an acceptable time, and event is added to your calendar.</span>
  </a><a class="result" href="/react-sketchapp">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6842/Screen_20Shot_202017-04-27_20at_205.58.06_20PM.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">React Sketch.app</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Managing the assets of design systems in Sketch is complex, error-prone and time consuming. Sketch is scriptable, but the API often changes. React provides the perfect wrapper to build reusable documents in a way already familiar to JavaScript developers.</span>
  </a><a class="result" href="/concrete5">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3907/9008b57334082bb616b345d910c95589_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">concrete5</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">171</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an open-source content management system for publishing content on the World Wide Web and intranets. It is designed for ease of use, for users with a minimum of technical skills. It enables users to edit site content directly from the page.</span>
  </a><a class="result" href="/mautic">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3849/Cv9FgWXU_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mautic</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">92</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an open marketing software platform that provides you with the greatest level of integration and deep audience intelligence, enabling you to make more meaningful customer connections. It Connects all your digital properties &amp; channels into a seamless customer experience. </span>
  </a><a class="result" href="/litmus">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/57/FlNaz6PN.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Litmus</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">34</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Litmus is a testing service for web and marketing professionals. It allows people to cross-browser test their websites, and test their email newsletters across a range of email clients and spam filters.</span>
  </a><a class="result" href="/onelogin">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1287/JXM14npm.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OneLogin</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">26</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">OneLogin provides a cloud-based identity and access management (IAM) solution that offers simple single sign-on (SSO), making it easier for companies to secure and manage access to web applications both in the cloud and behind the firewall. </span>
  </a><a class="result" href="/todoist">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1969/iJBA1-9j_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Todoist</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">8</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It lets you keep track of everything in one place. It gives you the confidence that everything’s organized and accounted for, so you can make progress on the things that are important to you.</span>
  </a><a class="result" href="/silverstripe">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3618/Cwz8nqxA_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">SilverStripe</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">130</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the intuitive content management system and flexible framework loved by editors and developers alike. Equip your web teams to achieve outstanding results.

</span>
  </a><a class="result" href="/abstract">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7300/WIrU3jiP_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Abstract</span>
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
    <span class="additional">Abstract builds upon and extends the stable technology of Git to host and manage your work.</span>
  </a><a class="result" href="/mediawiki">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2561/200px-Mediawiki_logo_reworked_2.svg_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">MediaWiki</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">108</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a free server-based software. It is an extremely powerful, scalable software and a feature-rich wiki implementation that uses PHP to process and display data stored in a database, such as MySQL.</span>
  </a><a class="result" href="/productboard">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3969/iSj8wV3F.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ProductBoard</span>
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
    <span class="additional">Organize and clearly structure all your qualitative research. Discover patterns in the jobs your users want to get done. Surface pains your product can eliminate, point out gains it can create, reveal your competition.</span>
  </a><a class="result" href="/uxpin">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/548/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">UXPin</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">21</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Agile UX in one place: design systems, prototyping, and documentation together</span>
  </a><a class="result" href="/targetprocess">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/533/DNCqk-h_.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Targetprocess</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">20</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Targetprocess is an agile project management software that focuses on information visualization and freedom. It helps to track projects using Scrum, Kanban or other agile practices.</span>
  </a><a class="result" href="/pipefy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3455/icon-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Pipefy</span>
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
    <span class="additional">With Pipefy, your team gets to choose how to run their processes. Pipefy is agile and lets you use the best of Kanban or scrum methods. Easily connect processes with other teams, plan sprints, view progress in burndown charts or with report</span>
  </a><a class="result" href="/hangouts">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5828/Hangouts_Icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Hangouts</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">19</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a communication platform which includes messaging, video chat, and VOIP features.</span>
  </a><a class="result" href="/passbolt">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4992/fxjngQyJ.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Passbolt</span>
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
    <span class="additional">Passbolt is an open source password manager for teams. It allows to securely store and share credentials, and is based on OpenPGP.</span>
  </a><a class="result" href="/quip">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1254/quip.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Quip</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">40</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Edit and discuss in one place. Quip combines documents with messages so you can work faster, on the web or on the go.</span>
  </a><a class="result" href="/google-hangouts-chat">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8558/mRHomqt.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Hangouts Chat</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">28</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Whether in a 1:1 chat or a dedicated group workspace, collaborate with your team in an organized way. Share and discuss Docs, Sheets, and Slides all in one place.</span>
  </a><a class="result" href="/affinity-designer">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4181/9DYUTxY7_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Affinity Designer</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">15</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">No bloat, no gimmicks, just all the tools you need, implemented how you always dreamed. It is a stripped back, pro-end workhorse that will always get your job done. It was created to thrive on the electric pace of the latest computing hardware. Live, responsive and incredibly fluid, it’s simply a joy to use.</span>
  </a><a class="result" href="/salesforce-marketing-cloud">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8520/mVUDo78h_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Salesforce Marketing Cloud</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">18</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Email marketing automation connects interactions from any channel or device, and combines customer data and behaviors to create real-time relevant communications.</span>
  </a><a class="result" href="/skype-for-business">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5437/m-mJKvsM_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Skype for Business</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">33</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With one click, anyone can join your online meeting, from any device. You can choose to meet right away, or schedule from Outlook for later. The meeting URL is personalized just for you.</span>
  </a><a class="result" href="/keystonejs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1230/d5575455853a3eb2ec1dafb5522ffc9a.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">KeystoneJS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">13</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Keystone is the easiest way to build database-driven websites, applications and APIs in Node.js.</span>
  </a><a class="result" href="/brave">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7577/rO7aIdyp_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Brave</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a fast, private and secure web browser for PC and mobile. It blocks ads and trackers. It prevents you from being tracked by sneaky advertisers, malware and pop-ups.</span>
  </a><a class="result" href="/netsuite">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/248/Xmp1cwhV_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">NetSuite</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">72</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">One complete system including accounting, CRM, inventory, and ecommerce. With NetSuite, you can implement the complete business software suite to run your entire business better or begin with one module and add functionality as you need it.</span>
  </a><a class="result" href="/join-me">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/161/we6o-6_N.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Join.me</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">25</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Get everybody on the same page, when they're not in the same room, instantly. Review documents and designs. Train staff. Demo products or just show off. join.me is a ridiculously simple screen sharing tool for meetings on the fly.</span>
  </a><a class="result" href="/expensify">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/284/343b01ca04f1539d018d83fb1dae0150.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Expensify</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">11</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Streamline the way your employees report expenses, the way expenses are approved,
and the way you export that information to your accounting package.</span>
  </a><a class="result" href="/mailtrap">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/506/VWjhZN6Z_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mailtrap</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">29</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Fake SMTP server for development teams to test, view and share emails sent from the development and staging environments without spamming real customers.</span>
  </a><a class="result" href="/bugzilla">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1362/osfnPuRC.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bugzilla</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">14</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Bugzilla is a "Defect Tracking System" or "Bug-Tracking System". Defect Tracking Systems allow individual or groups of developers to keep track of outstanding bugs in their product effectively. Most commercial defect-tracking software vendors charge enormous licensing fees. Despite being "free", Bugzilla has many features its expensive counterparts lack.</span>
  </a><a class="result" href="/hellosign">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1345/R5PcIJdS.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">HelloSign</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">31</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">HelloSign provides fast, secure, and legally binding eSignatures for Business. Our API gives you the ability to embed signing right into your own site with just a few lines of code. Set-up only takes minutes to complete.</span>
  </a><a class="result" href="/crisp">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5224/r5Kd_ifq.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Crisp</span>
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
    <span class="additional">Chat with website visitors, integrate your favorite tools, and deliver a great customer experience.
</span>
  </a><a class="result" href="/tweetdeck">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8855/_65QFl7B_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Tweetdeck</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">0</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The most powerful Twitter tool for real-time tracking, organizing, and engagement. Reach your audiences and discover the best of Twitter.From breaking news and entertainment to sports and politics, get the full story with all the live commentary.</span>
  </a><a class="result" href="/desk-com">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/71/l15HgTES.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Desk.com</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">44</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Desk.com lets you see all your customers in one place and engage them across all your support channels (Twitter, Facebook, phone, email, chat and discussion boards) in one easy-to-use desktop. Be there for your customers — anytime, anywhere.  </span>
  </a><a class="result" href="/podio">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/184/MMKYSo74.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Podio</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">21</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Podio is built to work like you. Pick your apps - from simple project management, to handling sales leads, to tracking job candidates. You’ll find hundreds more for any business process in the free Podio App Market. Organize your apps in unlimited workspaces. Add your team and even clients or contractors to get the job done together.</span>
  </a><a class="result" href="/codetree">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2464/p5YGhrfi.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Codetree</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">9</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Codetree is a project management app deeply integrated with GitHub issues -- every issue in Codetree corresponds directly to an issue on GitHub. We offer both a compact list view and kanban taskboards.</span>
  </a><a class="result" href="/umbraco">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2005/hIGLHjkE_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Umbraco</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">37</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a friendly open-source Content Management System and is one of the most widely used ASP.NET Content Management Systems. It is free and offers great flexibility and extensive capabilities.</span>
  </a><a class="result" href="/quickbooks">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3140/quickbooks-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">QuickBooks</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">24</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an accounting software package. You can access and manage your books from your computer, laptop, tablet, or smartphone anytime you choose. Create access privileges so that your colleague or accountant can login and work.</span>
  </a><a class="result" href="/screenhero">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/867/pUOTenr6.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Screenhero</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">18</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Screenhero gives you low-lag screen sharing, multiple mouse cursors, and voice chat. You each get your own mouse cursor, and you're both always in control. It works with your favorite IDE, text editor, or app.</span>
  </a><a class="result" href="/yammer">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/246/NWoiK8Kp.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Yammer</span>
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
    <span class="additional">Yammer brings the power of social networking to your company. Collaborate securely across departments, geographies, content and business applications.</span>
  </a><a class="result" href="/avocode">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2157/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Avocode</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Avocode is a cross-platform app that helps designers and developers collaborate and easily handoff designs. Avocode comes with 14 days free trial.</span>
  </a><a class="result" href="/sanity_2">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7890/nLVTfSj2_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sanity</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Sanity is a headless, real-time CMS where the editor is an open source React-based construction kit and the backend is a graph-oriented cloud datastore with a globally distributed CDN.</span>
  </a><a class="result" href="/hootsuite">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3391/cGUD9kwQ_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Hootsuite</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">16</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It manages all your social media in one place. From finding prospects to serving customers, it helps you do more with your social media. The system's user interface takes the form of a dashboard, and supports social network integrations.</span>
  </a><a class="result" href="/amazon-workspaces">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/416/16ffae8c667bdbc6a4969f6f02090652.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon WorkSpaces</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">With a few clicks in the AWS Management Console, customers can provision a high-quality desktop experience for any number of users at a cost that is highly competitive with traditional desktops and half the cost of most virtual desktop infrastructure (VDI) solutions. End-users can access the documents, applications and resources they need with the device of their choice, including laptops, iPad, Kindle Fire, or Android tablets.</span>
  </a><a class="result" href="/forestry">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7955/h8AfYODA_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Forestry</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a simple Git-based CMS for Jekyll and Hugo sites. Built for devs who hate bloat. It helps developers manage a content-based system into their websites seamlessly and there's also the benefits of collaborating with teams while at it.</span>
  </a><a class="result" href="/google-hangouts">
    <div style="display:inline-block">
      <img src="https://ucarecdn.com/4e2a74dc-9dfc-407c-aecf-c80656b7dbd9/">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Hangouts</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">18</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Message contacts, start free video or voice calls, and hop on a conversation with one person or a group.</span>
  </a><a class="result" href="/idonethis">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/338/2eee7fc35276d17fce76d9bbc9263981.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">iDoneThis</span>
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
    <span class="additional">Every evening, iDoneThis sends you an email that asks you what you got done that day. The next morning, we send a digest of what everyone on your team got done the previous day to you and your team members. </span>
  </a><a class="result" href="/htmltowordpress">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4081/Tla1Uq2w.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">HTML to Wordpress</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Htmltowordpress.io is a cloud-based tool that converts your current HTML based website into a Wordpress theme in seconds. Same site, same content, just as an editable Wordpress theme. If you have at least one html file you are ready to start the conversion process.</span>
  </a><a class="result" href="/teamviewer">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3174/ML2OvUjZ_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">TeamViewer</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">19</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Its aproprietary software for remote control, desktop sharing, online meetings, web conferencing and file transfer between computers.</span>
  </a><a class="result" href="/glide-2">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/10365/j5RptoTm_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Glide </span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Pick a sheet, customize your app, share it with a link. Add your data to the sheet and share your custom app! Only pay for apps that need whitelabeling or store distribution.</span>
  </a><a class="result" href="/axure-2">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3351/IzpAFFGV_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Axure </span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">24</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The way to plan, prototype, and hand off to developers, all without code. A wireframing, rapid prototyping, documentation and specification software tool aimed at web, mobile and desktop applications. </span>
  </a><a class="result" href="/quora">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5379/nBalwThK_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Quora</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It connects you to everything you want to know about. Quora aims to be the easiest place to write new content and share content from the web. We organize people and their interests so you can find, collect and share the information most valuable to you.</span>
  </a><a class="result" href="/hackpad">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/289/oo1SaTNQ.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">HackPad</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">14</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Hackpad is a smart collaborative workspace that your team will love.</span>
  </a><a class="result" href="/affinity-photo">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5415/9DYUTxY7_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Affinity Photo</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is born to work hand-in-hand with the latest powerful computer technology, it’s fully-loaded photo editor integrated across macOS, Windows and iOS.</span>
  </a><a class="result" href="/twitter-ads">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5145/gaj36XL5_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Twitter Ads</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">15</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">You can create engagement, measure results, and attract new followers or website visitors, with no minimum spend. You can grow your influence steadily without ever having to manage a campaign.</span>
  </a><a class="result" href="/zoho">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5654/B4cJBv28_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Zoho</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">14</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Unique and powerful suite of software to run your entire business. It contains word processing, spreadsheets, presentations, databases, note-taking, wikis, web conferencing, customer relationship management, project management, invoicing, and other applications.</span>
  </a><a class="result" href="/keybase-teams">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7630/LgqWvzCQ_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Keybase Teams</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">9</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Keybase is for anyone. Imagine a Slack for the whole world, except end-to-end encrypted across all your devices. Or a Team Dropbox where the server can't leak your files or be hacked.</span>
  </a><a class="result" href="/gusto">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/235/ponSaulf.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gusto</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">28</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">ZenPayroll is delightful, modern payroll. Our comprehensive payroll service enables businesses to get set up and run payroll in minutes, from any web enabled device. All government payroll taxes and reporting are taken care of automatically and paperlessly. We've processed millions of dollars in payroll and our customers span a wide variety of businesses, from flower shops to technology start-ups. We would be delighted to provide you modern payroll.</span>
  </a><a class="result" href="/cockpit">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/979/e5b082839e7ec5541016a9813bbeb4b8.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Cockpit</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">An API-driven CMS without forcing you  to make compromises in how you implement your site. The CMS for developers. Manage content like collections, regions, forms and galleries which you can reuse anywhere on your website.</span>
  </a><a class="result" href="/processwire">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3504/tgOfWtM1.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ProcessWire</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">ProcessWire is an open source content management system (CMS) and web application framework aimed at the needs of designers, developers and their clients. ProcessWire gives you more control over your fields, templates and markup than other platforms, and provides a powerful template system that works the way you do</span>
  </a><a class="result" href="/aircall">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3332/logo-slack.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Aircall</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">18</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Aircall is an app that you can install and setup in a few minutes. It lets you buy one or several phone numbers across the world, add teammates to your dashboard, and place &amp; receive calls on your existing devices. Everything is managed inside the Aircall app.</span>
  </a><a class="result" href="/service-now">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3769/hf0MaWmi_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Service-Now</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">18</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It makes work, work better for people. Transform old, manual ways of working into modern digital workflows, so employees and customers get what they need, when they need it—fast, simple, easy.
</span>
  </a><a class="result" href="/dashlane">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1284/view_2x.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Dashlane</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Dashlane is a password manager and online security app for everyone who lives, works, and plays on the internet.</span>
  </a><a class="result" href="/pendo">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4378/RwIcCGrB_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Pendo</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Use Pendo to create more engaging products.  With absolutely no coding, understand everything your customers do in your product and use in-app messages to increase engagement.</span>
  </a><a class="result" href="/haiku">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8476/btWKs0xk_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Haiku</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Create dynamic, cross-platforms UIs using design tools, code, or both.</span>
  </a><a class="result" href="/amazon-connect">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6732/amazon-connect.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon Connect</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The self-service graphical interface in Amazon Connect makes it easy for non-technical users to design contact flows, manage agents, and track performance metrics – no specialized skills required. </span>
  </a><a class="result" href="/front">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1376/giGwJ9Wq_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Front</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">24</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Front allows you to collaborate with your team, stay productive, and use email and social together. Currently available on Mac, Windows, Web, and Mobile.</span>
  </a><a class="result" href="/doodle">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/940/GcZQQBaj.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Doodle</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Doodle takes the pain out of finding the right date and time for a group of people to meet and makes scheduling virtually effortless. More than 20M people use Doodle every month around the globe for private and business meetings. </span>
  </a><a class="result" href="/inkscape">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4120/chDAoUGH_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Inkscape</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is professional quality vector graphics software which runs on Windows, Mac OS X and Linux. This software can be used to create or edit vector graphics such as illustrations, diagrams, line arts, charts, logos and complex paintings.</span>
  </a><a class="result" href="/statamic">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3022/c6381bac52d507597b83306326b20e21.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Statamic</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Statamic 2 is now built on Laravel and sporting a brand new Vue.js-powered control panel. As a developer you can build, configure, and manage everything right in your code editor. As a client or content manager you never have to leave the c</span>
  </a><a class="result" href="/streak">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/31/logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Streak</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">13</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Streak lets you keep track of all your deals right from your inbox. We let you group emails from the same customer together into one view and push that customer through your pipeline. </span>
  </a><a class="result" href="/wrike">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1724/xvVVUP8E_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Wrike</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Cloud-based collaboration and project management software that scales across teams in any business.</span>
  </a><a class="result" href="/proto-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/505/WvPwQzE1_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Proto.io</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">13</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Proto.io supports all the major mobile gestures and touch events like tap, tap-hold, swipe, pinch, and zoom. Interaction designers are not limited to a single ‘link’ transition anymore. Instead they can apply animated screen transitions like slide, fade, pop, flip, flow, and turn.</span>
  </a><a class="result" href="/craftcms">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4862/ds8IotBg_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Craft CMS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a flexible, user-friendly CMS for creating custom digital experiences on the web and beyond. It is a WordPress alternative for development-oriented publishers who want deeper control and more powerful performance from their content management tools. It is built to be exceptionably scalable, and offers native features for complex content management relationships.</span>
  </a><a class="result" href="/typo3">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2942/tisWILkq_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Typo3</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">27</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a free and open-source Web content management system written in PHP. It can run on several web servers, such as Apache or IIS, on top of many operating systems, among them Linux, Microsoft Windows, FreeBSD, macOS and OS/2.</span>
  </a><a class="result" href="/groovehq">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/74/4vehL4fy_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Groove</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">37</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Build better customer experiences with Groove</span>
  </a><a class="result" href="/wekan">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4427/-NNP9RC0.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Wekan</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Whether you’re maintaining a personal todo list, planning your holidays with some friends, or working in a team on your next revolutionary idea, Kanban boards are an unbeatable tool to keep your things organized. They give you a visual overview of the current state of your project, and make you productive by allowing you to focus on the few items that matter the most.</span>
  </a><a class="result" href="/twill">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9249/01_twill_facebook_profile.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Twill</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Twill is an open source CMS toolkit for Laravel that helps developers rapidly create a custom admin console that is intuitive, powerful and flexible. </span>
  </a><a class="result" href="/aem">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6365/6u8P7Pr6_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AEM</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">9</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a web-based client-server system for building, managing and deploying commercial websites and related services. It combines a number of infrastructure-level and application-level functions into a single integrated package.  </span>
  </a><a class="result" href="/flow">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/185/no-img-open-source.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Flow</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">13</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Flow is an online collaboration platform that makes it easy for people to create, organize, discuss, and accomplish tasks with anyone, anytime, anywhere. By merging a sleek, intuitive interface with powerful functionality, we're out to revolutionize the way the world's productive teams get things done.</span>
  </a><a class="result" href="/gitkraken-glo">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9212/LRrR48qp_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GitKraken Glo</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A more productive way for developers to track tasks and issues from inside GitKraken, VS Code, Atom or a browser! Glo Boards sync in real-time with GitHub Issues, support markdown and offer lots of time-saving features for devs.</span>
  </a><a class="result" href="/protopie">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/10251/bS8jfuhu_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ProtoPie</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the easiest tool used to turn your UI/UX design ideas into highly interactive prototypes for mobile, desktop, web, all the way to IoT. ProtoPie runs on macOS &amp; Windows and the player app is on iOS and Android.</span>
  </a><a class="result" href="/autopilothq">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3162/B4omzVTi.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AutopilotHQ</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">20</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Autopilot’s intuitive drag and drop Journey canvas allows you to send the right message, on the right channel, at the right time. Automate your marketing, send personalized messages, build workflow and process in Salesforce, and more.</span>
  </a><a class="result" href="/sugarcrm">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/33/aqcFdWXX.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">SugarCRM</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">14</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Manage your sales, marketing, and customer support better with SugarCRM's online CRM software. </span>
  </a><a class="result" href="/sprint-ly">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3/ef30ac2478cb8b25b43f2bb554159e07.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sprint.ly</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Sprint.ly is an innovative new way to manage products.</span>
  </a><a class="result" href="/vmware-horizon-suite">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/417/xxr1e-Lu_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">VMware Horizon Suite</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Stimulate workforce productivity by delivering a consistent, intuitive, and collaborative computing experience across all devices—anytime, anywhere. Manage, secure and back up end-user assets and applications from one place. Protect against compliance risk with policy-driven access. Streamline and simplify operations by turning disparate operating systems, applications, and data into centralized services delivered on any device.</span>
  </a><a class="result" href="/swiftlint">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8243/XzDXMlHD_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">SwiftLint</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">20</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a tool to enforce Swift style and conventions, loosely based on GitHub's Swift Style Guide.It hooks into Clang and SourceKit to use the AST representation of your source files for more accurate results.</span>
  </a><a class="result" href="/sendinblue">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5639/bKUohNb7_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">SendinBlue</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">26</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a digital marketing toolbox that's built to scale and adapt with you as you grow. You can save time and boost performance by automating your segmentation and marketing messages.

</span>
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
data.to_csv('C:/Users/i9i91/OneDrive/바탕 화면/github 저장내용/portfolio.io/크롤링4.csv')  




