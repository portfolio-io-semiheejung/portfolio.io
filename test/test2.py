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
<div class="totals total-all text-right">253 results</div>
<a class="result" href="/postman">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1336/xWMRvm_5_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Postman</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3077</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the only complete API development environment, used by nearly five million developers and more than 100,000 companies worldwide. </span>
  </a><a class="result" href="/stack-overflow">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1927/so-icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Stack Overflow</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1267</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Stack Overflow is a question and answer site for professional and enthusiast programmers. It's built and run by you as part of the Stack Exchange network of Q&amp;A sites. With your help, we're working together to build a library of detailed answers to every question about programming.</span>
  </a><a class="result" href="/google-maps">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1652/googlemaps.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Maps</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7625</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Create rich applications and stunning visualisations of your data, leveraging the comprehensiveness, accuracy, and usability of Google Maps and a modern web platform that scales as you grow.</span>
  </a><a class="result" href="/elasticsearch">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/841/Image_2019-05-20_at_4.58.04_PM.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Elasticsearch</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3139</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Elasticsearch is a distributed, RESTful search and analytics engine capable of storing data and searching it in near real time. Elasticsearch, Kibana, Beats and Logstash are the Elastic Stack (sometimes called the ELK Stack). </span>
  </a><a class="result" href="/github-pages">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/683/sBsvBbjY.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GitHub Pages</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1507</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Public webpages hosted directly from your GitHub repository. Just edit, push, and your changes are live.</span>
  </a><a class="result" href="/amazon-route-53">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/38/amazon-route-53.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon Route 53</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2196</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon Route 53 is designed to give developers and businesses an extremely reliable and cost effective way to route end users to Internet applications by translating human readable names like www.example.com into the numeric IP addresses like 192.0.2.1 that computers use to connect to each other. Route 53 effectively connects user requests to infrastructure running in Amazon Web Services (AWS) – such as an Amazon Elastic Compute Cloud (Amazon EC2) instance, an Amazon Elastic Load Balancer, or an Amazon Simple Storage Service (Amazon S3) bucket – and can also be used to route users to infrastructure outside of AWS.</span>
  </a><a class="result" href="/shopify">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/266/xDoyHgZW_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Shopify</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4162</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Shopify powers tens of thousands of online retailers including General Electric, Amnesty International, CrossFit, Tesla Motors, Encyclopaedia Britannica, Foo Fighters, GitHub, and more. Our platform allows users to easily and quickly create their own online store without all the technical work involved in developing their own website, or the huge expense of having someone else build it. Shopify lets merchants manage all aspects of their shops: uploading products, changing the design, accepting credit card orders, and viewing their incoming orders and completed transactions.</span>
  </a><a class="result" href="/woocommerce">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3139/y2hg0gx5_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">WooCommerce</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4908</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">WooCommerce is the most popular WordPress eCommerce plugin. And it's available for free. Packed full of features, perfectly integrated into your self-hosted WordPress website.</span>
  </a><a class="result" href="/tensorflow">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4717/FtFnqC38_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">TensorFlow</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">351</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">TensorFlow is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) communicated between them. The flexible architecture allows you to deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device with a single API.</span>
  </a><a class="result" href="/magento">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1769/wcU6vWxh_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Magento</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2217</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Magento Community Edition is perfect if you’re a developer who wants to build your own solution with flexible eCommerce technology. You can modify the core code and add a wide variety of features and functionality.</span>
  </a><a class="result" href="/disqus">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/29/af69f7089ebfabe3bb33129bf9d4d325.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Disqus</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2050</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Disqus looks to make it very easy and rewarding for people to interact on websites using its system. Commenters can build reputation and carry their contributions from one website to the next. </span>
  </a><a class="result" href="/namecheap">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/40/sSwMqqsH.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Namecheap</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1982</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">We provide a set of DNS servers spread across the US and Europe to deliver highly reliable DNS services to everyone. By choosing Namecheap.com as your domain registrar, you are choosing a highly reputable and reliable partner. Namecheap.com is rated 4.6 out of 5 - Based on 1,395 reviews via Google Checkout</span>
  </a><a class="result" href="/netlify">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2748/lV55uZMx.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Netlify</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">598</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Netlify is smart enough to process your site and make sure all assets gets optimized and served with perfect caching-headers from a cookie-less domain. We make sure your HTML is served straight from our CDN edge nodes without any round-trip to our backend servers and are the only ones to give you instant cache invalidation when you push a new deploy. Netlify is also the only static hosting service with integrated continuous deployment.</span>
  </a><a class="result" href="/google-cloud-dns">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/696/s01TMTGn.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Cloud DNS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1864</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Use Google's infrastructure for production quality, high volume DNS serving. Your users will have reliable, low-latency access to Google's infrastructure from anywhere in the world using our network of Anycast name servers.</span>
  </a><a class="result" href="/dns-made-easy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1685/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">DNS Made Easy</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2534</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">DNS Made Easy is a subsidiary of Tiggee LLC, and is a world leader in providing global IP Anycast enterprise DNS services. DNS Made Easy is currently ranked the fastest provider for 8 consecutive months and the most reliable provider.</span>
  </a><a class="result" href="/lets-encrypt">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4225/lSuJvwXU_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Let's Encrypt</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">459</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a free, automated, and open certificate authority brought to you by the non-profit Internet Security Research Group (ISRG).
</span>
  </a><a class="result" href="/jekyll">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1114/ad968c1615d956e800fa36494314f48c.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Jekyll</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">273</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Think of Jekyll as a file-based CMS, without all the complexity. Jekyll takes your content, renders Markdown and Liquid templates, and spits out a complete, static website ready to be served by Apache, Nginx or another web server. Jekyll is the engine behind GitHub Pages, which you can use to host sites right from your GitHub repositories.</span>
  </a><a class="result" href="/squarespace">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/178/huJH2lyt_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Squarespace</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1744</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Whether you need simple pages, sophisticated galleries, a professional blog, or want to sell online, it all comes standard with your Squarespace website. Squarespace starts you with beautiful designs right out of the box — each handcrafted by our award-winning design team to make your content stand out.</span>
  </a><a class="result" href="/swagger-ui">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3417/pIea9Ji0.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Swagger UI</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">364</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Swagger UI is a dependency-free collection of HTML, Javascript, and CSS assets that dynamically generate beautiful documentation and sandbox from a Swagger-compliant API</span>
  </a><a class="result" href="/auth0">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/601/5Nm3jtVh.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Auth0</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">222</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A set of unified APIs and tools that instantly enables Single Sign On and user management to all your applications.</span>
  </a><a class="result" href="/algolia">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/589/iEEMVN5L_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Algolia</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">397</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Our mission is to make you a search expert. Push data to our API to make it searchable in real time. Build your dream front end with one of our web or mobile UI libraries. Tune relevance and get analytics right from your dashboard.</span>
  </a><a class="result" href="/dyn">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/37/fsKWm_AI_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Dyn</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1637</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">An all-in-one Managed DNS service for your registered domain names. Dyn DNS is the perfect solution for your domain name’s DNS needs, whether it is for personal or business use. It gives you complete control over your DNS zone and its associated DNS records, complete with a simple DNS management web interface.
</span>
  </a><a class="result" href="/leaflet">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2392/leaflet_upic.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Leaflet</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">626</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Leaflet is an open source JavaScript library for mobile-friendly interactive maps. It is developed by Vladimir Agafonkin of MapBox with a team of dedicated contributors. Weighing just about 30 KB of gzipped JS code, it has all the features most developers ever need for online maps.</span>
  </a><a class="result" href="/amazon-api-gateway">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3299/aws-api-gateway.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon API Gateway</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">317</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, authorization and access control, monitoring, and API version management.</span>
  </a><a class="result" href="/aws-iam">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/418/aws-iam.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS IAM</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">259</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AWS Identity and Access Management.</span>
  </a><a class="result" href="/jupyter">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4190/fGBUdNf__400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Jupyter</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">168</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The Jupyter Notebook is a web-based interactive computing platform. The notebook combines live code, equations, narrative text, visualizations, interactive dashboards and other media.</span>
  </a><a class="result" href="/arduino">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3195/9d19310763171b0d958d23a18b3d7e1c.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Arduino</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">68</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Arduino is an open-source electronics prototyping platform based on flexible, easy-to-use hardware and software.</span>
  </a><a class="result" href="/keras">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5601/keras.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Keras</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">104</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Deep Learning library for Python. Convnets, recurrent neural networks, and more. Runs on TensorFlow or Theano. https://keras.io/</span>
  </a><a class="result" href="/scikit-learn">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2657/scikit-learn-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">scikit-learn</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">140</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">scikit-learn is a Python module for machine learning built on top of SciPy and distributed under the 3-Clause BSD license.</span>
  </a><a class="result" href="/pytorch">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8171/YYpjkbVn_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PyTorch</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">68</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">PyTorch is not a Python binding into a monolothic C++ framework. It is built to be deeply integrated into Python. You can use it naturally like you would use numpy / scipy / scikit-learn etc.</span>
  </a><a class="result" href="/solr">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1596/al3IkKF8.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Solr</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">190</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Solr is the popular, blazing fast open source enterprise search platform from the Apache Lucene project. Its major features include powerful full-text search, hit highlighting, faceted search, near real-time indexing, dynamic clustering, database integration, rich document (e.g., Word, PDF) handling, and geospatial search. Solr is highly reliable, scalable and fault tolerant, providing distributed indexing, replication and load-balanced querying, automated failover and recovery, centralized configuration and more. Solr powers the search and navigation features of many of the world's largest internet sites.</span>
  </a><a class="result" href="/mapbox">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1640/cvosutVr_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mapbox</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">147</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">We make it possible to pin travel spots on Pinterest, find restaurants on Foursquare, and visualize data on GitHub.</span>
  </a><a class="result" href="/amazon-kinesis">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/433/16ffae8c667bdbc6a4969f6f02090652.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon Kinesis</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">224</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon Kinesis can collect and process hundreds of gigabytes of data per second from hundreds of thousands of sources, allowing you to easily write applications that process information in real-time, from sources such as web site click-streams, marketing and financial information, manufacturing instrumentation and social media, and operational logs and metering data. </span>
  </a><a class="result" href="/godaddy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/42/eH9oma1K.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">GoDaddy</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">70</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Go Daddy makes registering Domain Names fast, simple, and affordable</span>
  </a><a class="result" href="/amazon-cognito">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1093/16ffae8c667bdbc6a4969f6f02090652.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon Cognito</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">113</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">You can create unique identities for your users through a number of public login providers (Amazon, Facebook, and Google) and also support unauthenticated guests. You can save app data locally on users’ devices allowing your applications to work even when the devices are offline.</span>
  </a><a class="result" href="/insomnia-rest-client">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6406/qLPJL1NZ.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Insomnia REST Client</span>
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
    <span class="additional">Insomnia is a powerful REST API Client with cookie management, environment variables, code generation, and authentication for Mac, Window, and Linux.</span>
  </a><a class="result" href="/devise">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1432/devise.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Devise</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">196</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Devise is a flexible authentication solution for Rails based on Warden</span>
  </a><a class="result" href="/weebly">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/176/ajoQm8C7_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Weebly</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">419</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Weebly is an AJAX website creator that allows you to create pages with template skins and content widgets. Users can easily drag-and-drop content widgets like pictures, text, video and Google Maps in WYSIWYG-fashion. </span>
  </a><a class="result" href="/prestashop">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/925/C6U2rHtG_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PrestaShop</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">313</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">PrestaShop is written in PHP, is highly customizable, supports all the major payment services, is translated in many languages and localized for many countries, and is fully responsive (both front- and back-office).</span>
  </a><a class="result" href="/keycloak">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5439/oAC05cEB_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Keycloak</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">41</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an Open Source Identity and Access Management For Modern Applications and Services. It adds authentication to applications and secure services with minimum fuss. No need to deal with storing users or authenticating users. It's all available out of the box.


</span>
  </a><a class="result" href="/amazon-elasticsearch-service">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3736/amazon-elasticsearch-service.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon Elasticsearch Service</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">142</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon Elasticsearch Service is a fully managed service that makes it easy for you to deploy, secure, and operate Elasticsearch at scale with zero down time.</span>
  </a><a class="result" href="/vercel">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7618/bHjpwZem_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Vercel</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">59</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A cloud platform for serverless deployment. It enables developers to host websites and web services that deploy instantly, scale automatically, and require no supervision, all with minimal configuration.</span>
  </a><a class="result" href="/webflow">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/587/truotQk9.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Webflow</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">49</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Webflow is a responsive design tool that lets you design, build, and publish websites in an intuitive interface. Clean code included!</span>
  </a><a class="result" href="/vuepress">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8863/paeckCWC.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">VuePress</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">18</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A minimalistic static site generator with a Vue-powered theming system, and a default theme optimized for writing technical documentation. It was created to support the documentation needs of Vue's own sub projects.</span>
  </a><a class="result" href="/apiary">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/272/7b176017eab2903a23d914460b6dd600.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apiary</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">66</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It takes more than a simple HTML page to thrill your API users. The right tools take weeks of development. Weeks that apiary.io saves.</span>
  </a><a class="result" href="/inspectlet">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2439/kfind.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Inspectlet</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">400</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Inspectlet records videos of your visitors as they use your site, allowing you to see everything they do. See every mouse movement, scroll, click, and keypress on your site. You never need to wonder how visitors are using your site again.</span>
  </a><a class="result" href="/raspberry-pi">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5174/LcSgue9p_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Raspberry Pi</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">35</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A low cost, credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse. It is a capable little device that enables people of all ages to explore computing, and to learn how to program in languages like Scratch and Python.</span>
  </a><a class="result" href="/openstreetmap">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2068/OSM_fixed_512.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OpenStreetMap</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">61</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">OpenStreetMap is built by a community of mappers that contribute and maintain data about roads, trails, cafés, railway stations, and much more, all over the world.</span>
  </a><a class="result" href="/paw">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2032/YApveawR.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Paw</span>
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
    <span class="additional">Paw is a full-featured and beautifully designed Mac app that makes interaction with REST services delightful. Either you are an API maker or consumer, Paw helps you build HTTP requests, inspect the server's response and even generate client code.</span>
  </a><a class="result" href="/lottie">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6445/lottie.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Lottie</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">29</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Lottie is a mobile library for Android and iOS that parses Adobe After Effects animations exported as json with Bodymovin and renders them natively on mobile!</span>
  </a><a class="result" href="/framer">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/826/BlCZdW9q.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Framer</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">29</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Framer is a JavaScript framework that makes creating realistic prototypes a breeze – complete with filters, spring physics and full 3D effects. Framer Generator is a desktop app that imports the resources and folder hierarchy from Photoshop files (Sketch coming soon). Import your design and immediately start to add interaction and animation.</span>
  </a><a class="result" href="/passport">
    <div style="display:inline-block">
      <img src="https://ucarecdn.com/8f3cac0e-b146-4f0f-878c-680a6671d804/">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Passport</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">30</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is authentication middleware for Node.js. Extremely flexible and modular, It can be unobtrusively dropped in to any Express-based web application. A comprehensive set of strategies support authentication using a username and password, Facebook, Twitter, and more.</span>
  </a><a class="result" href="/sphinx">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1598/TtqoAo1V.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sphinx</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">61</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It lets you either batch index and search data stored in an SQL database, NoSQL storage, or just files quickly and easily — or index and search data on the fly, working with it pretty much as with a database server.</span>
  </a><a class="result" href="/openlayers">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3208/397ce8027eb036960f00dd5153d41993.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OpenLayers</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">62</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">An opensource javascript library to load, display and render maps from multiple sources on web pages.</span>
  </a><a class="result" href="/jmeter-tool">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5839/8mAJQD05_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache JMeter</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">53</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is open source software, a 100% pure Java application designed to load test functional behavior and measure performance. It was originally designed for testing Web Applications but has since expanded to other test functions.</span>
  </a><a class="result" href="/stream">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2213/mBSAJI_h_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Stream</span>
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
    <span class="additional">Stream allows you to build scalable feeds, activity streams, and chat. Stream’s simple, yet powerful API’s and SDKs are used by some of the largest and most popular applications for feeds and chat. SDKs available for most popular languages.</span>
  </a><a class="result" href="/azure-machine-learning">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1221/azure-machine-learning.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Azure Machine Learning</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">26</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Azure Machine Learning is a fully-managed cloud service that enables data scientists and developers to efficiently embed predictive analytics into their applications, helping organizations use massive data sets and bring all the benefits of the cloud to machine learning.</span>
  </a><a class="result" href="/omniauth">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1433/omniauth.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OmniAuth</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">63</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">OmniAuth is a Ruby authentication framework aimed to abstract away the difficulties of working with various types of authentication providers. It is meant to be hooked up to just about any system, from social networks to enterprise systems to simple username and password authentication.</span>
  </a><a class="result" href="/zeppelin">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3659/NukVX4E1_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache Zeppelin</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">29</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A web-based notebook that enables interactive data analytics. You can make beautiful data-driven, interactive and collaborative documents with SQL, Scala and more.</span>
  </a><a class="result" href="/gatling">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3265/CR5gILun_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gatling</span>
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
    <span class="additional">Gatling is a highly capable load testing tool. It is designed for ease of use, maintainability and high performance.

Out of the box, Gatling comes with excellent support of the HTTP protocol that makes it a tool of choice for load testing any HTTP server. As the core engine is actually protocol agnostic, it is perfectly possible to implement support for other protocols. For example, Gatling currently also ships JMS support.</span>
  </a><a class="result" href="/kubeflow">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8052/EE9PAsVm_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Kubeflow</span>
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
    <span class="additional">The Kubeflow project is dedicated to making Machine Learning on Kubernetes easy, portable and scalable by providing a straightforward way for spinning up best of breed OSS solutions. </span>
  </a><a class="result" href="/tensorflow-js">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8762/q8sc1KuZ_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">TensorFlow.js</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">18</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Use flexible and intuitive APIs to build and train models from scratch using the low-level JavaScript linear algebra library or the high-level layers API</span>
  </a><a class="result" href="/aws-data-pipeline">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/422/aws-data-pipeline.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS Data Pipeline</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">24</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AWS Data Pipeline is a web service that provides a simple management system for data-driven workflows. Using AWS Data Pipeline, you define a pipeline composed of the “data sources” that contain your data, the “activities” or business logic such as EMR jobs or SQL queries, and the “schedule” on which your business logic executes. For example, you could define a job that, every hour, runs an Amazon Elastic MapReduce (Amazon EMR)–based analysis on that hour’s Amazon Simple Storage Service (Amazon S3) log data, loads the results into a relational database for future lookup, and then automatically sends you a daily summary email. </span>
  </a><a class="result" href="/runscope">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/278/zlcbgqTt.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Runscope</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">53</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Keep tabs on all aspects of your API's performance with uptime monitoring, integration testing, logging and real-time monitoring.</span>
  </a><a class="result" href="/amazon-sagemaker">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7967/amazon-sagemaker.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon SageMaker</span>
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
    <span class="additional">A fully-managed service that enables developers and data scientists to quickly and easily build, train, and deploy machine learning models at any scale.</span>
  </a><a class="result" href="/aws-step-functions">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6089/SWF-e64610d24b6e458c257f1105d8aa926f4a524182.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS Step Functions</span>
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
    <span class="additional">AWS Step Functions makes it easy to coordinate the components of distributed applications and microservices using visual workflows. Building applications from individual components that each perform a discrete function lets you scale and change applications quickly.</span>
  </a><a class="result" href="/aws-kms">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1907/aws-kms-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS Key Management Service</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">65</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data, and uses Hardware Security Modules (HSMs) to protect the security of your keys. AWS Key Management Service is integrated with other AWS services including Amazon EBS, Amazon S3, and Amazon Redshift. AWS Key Management Service is also integrated with AWS CloudTrail to provide you with logs of all key usage to help meet your regulatory and compliance needs. </span>
  </a><a class="result" href="/lucene">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1597/lucene.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Lucene</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">40</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Lucene Core, our flagship sub-project, provides Java-based indexing and search technology, as well as spellchecking, hit highlighting and advanced analysis/tokenization capabilities.</span>
  </a><a class="result" href="/dnsimple">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/36/HQM41T6C_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">DNSimple</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">69</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">DNSimple provides the tools you need to manage your domains. We offer both a carefully crafted web interface for managing your domains and DNS records, as well as an HTTP API with various code libraries and tools.
Buy, connect, operate!</span>
  </a><a class="result" href="/readme-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1570/B_fNbAwR.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ReadMe.io</span>
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
    <span class="additional">Collaborative Developer Hubs</span>
  </a><a class="result" href="/swiftype">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/227/Yn4nI9Oy.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Swiftype</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">166</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Swiftype is the easiest way to add great search to your website or mobile application.</span>
  </a><a class="result" href="/authy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/364/J64iXv8S.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Authy</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">29</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">We make the best rated Two-Factor Authentication smartphone app for consumers, a Rest API for developers and a strong authentication platform for the enterprise.</span>
  </a><a class="result" href="/mlflow">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9078/mlflow.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">MLflow</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">MLflow is an open source platform for managing the end-to-end machine learning lifecycle.</span>
  </a><a class="result" href="/gitbook">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2484/2r9Bf4lE_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gitbook</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">31</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a modern documentation platform where teams can document everything from products, to APIs and internal knowledge-bases. It is a place to think and track ideas for you &amp; your team.</span>
  </a><a class="result" href="/spacy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7312/7-7zis8f_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">SpaCy</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">21</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a library for advanced Natural Language Processing in Python and Cython. It's built on the very latest research, and was designed from day one to be used in real products. It comes with pre-trained statistical models and word vectors, and currently supports tokenization for 49+ languages. </span>
  </a><a class="result" href="/raml">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4083/JSGv7dnx.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">RAML</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">25</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">RESTful API Modeling Language (RAML) makes it easy to manage the whole API lifecycle from design to sharing. It's concise - you only write what you need to define - and reusable. It is machine readable API design that is actually human friendly.</span>
  </a><a class="result" href="/cuda">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2836/LUOWehvo_400x400.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">CUDA</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">57</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A parallel computing platform and application programming interface model,it enables developers to speed up compute-intensive applications by harnessing the power of GPUs for the parallelizable part of the computation.</span>
  </a><a class="result" href="/scrapy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3116/LJ_Gsz28_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Scrapy</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">19</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the most popular web scraping framework in Python. An open source and collaborative framework for extracting the data you need from websites. In a fast, simple, yet extensible way.</span>
  </a><a class="result" href="/amazon-glacier">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/387/amazon-glacier.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon Glacier</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">34</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">In order to keep costs low, Amazon Glacier is optimized for data that is infrequently accessed and for which retrieval times of several hours are suitable. With Amazon Glacier, customers can reliably store large or small amounts of data for as little as $0.01 per gigabyte per month, a significant savings compared to on-premises solutions.</span>
  </a><a class="result" href="/alfred">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2786/9fb69dcff86624e62ecaaa58c363e15b_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Alfred</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A productivity application for macOS, which boosts your efficiency with hotkeys, keywords and text expansion. Search your Mac and the web, and control your Mac using custom actions with the Powerpack.</span>
  </a><a class="result" href="/surge">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3646/W-ShR64-.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Surge</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">16</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Surge makes it easy for developers to deploy projects to a production-quality CDN through Grunt, Gulp, npm.</span>
  </a><a class="result" href="/amazon-cloudsearch">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/393/amazon-cloudsearch.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon CloudSearch</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">24</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon CloudSearch enables you to search large collections of data such as web pages, document files, forum posts, or product information. With a few clicks in the AWS Management Console, you can create a search domain, upload the data you want to make searchable to Amazon CloudSearch, and the search service automatically provisions the required technology resources and deploys a highly tuned search index.</span>
  </a><a class="result" href="/soap-ui">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3891/-AvocOY1_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Soap UI</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">25</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an open source functional Testing tool for API Testing. It supports multiple protocols such as SOAP, REST, HTTP, JMS, AMF and JDBC. It supports functional tests, security tests, and virtualization.</span>
  </a><a class="result" href="/docusaurus">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8438/xyht_7gq_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Docusaurus</span>
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
    <span class="additional">Docusaurus is a project for easily building, deploying, and maintaining open source project websites.

</span>
  </a><a class="result" href="/azure-search">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1370/azure-search.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Azure Search</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">20</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Azure Search makes it easy to add powerful and sophisticated search capabilities to your website or application. Quickly and easily tune search results and construct rich, fine-tuned ranking models to tie search results to business goals. Reliable throughput and storage provide fast search indexing and querying to support time-sensitive search scenarios.</span>
  </a><a class="result" href="/json-server">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/no-img-open-source.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">JSON Server</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Created with &lt;3 for front-end developers who need a quick back-end for prototyping and mocking.</span>
  </a><a class="result" href="/read-the-docs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/384/OhsWgbsr.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Read the Docs</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">14</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It hosts documentation, making it fully searchable and easy to find. You can import your docs using any major version control system, including Mercurial, Git, Subversion, and Bazaar.</span>
  </a><a class="result" href="/h2o">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5001/DTgFCs-n_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">H2O</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">13</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">H2O.ai is the maker behind H2O, the leading open source machine learning platform for smarter applications and data products. H2O operationalizes data science by developing and deploying algorithms and models for R, Python and the Sparkling Water API for Spark.</span>
  </a><a class="result" href="/jsdoc">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4047/js-doc.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">jsdoc</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">16</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">JSDoc 3 is an API documentation generator for JavaScript, similar to JavaDoc or PHPDoc. You add documentation comments directly to your source code, right along side the code itself. The JSDoc Tool will scan your source code, and generate a complete HTML documentation website for you.</span>
  </a><a class="result" href="/clearbit">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3227/boQMtD4j_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Clearbit</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">23</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Clearbit builds business intelligence APIs. Retrieve social data from emails and look up company information from domains.</span>
  </a><a class="result" href="/charles">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2493/charles_icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Charles</span>
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
    <span class="additional">Charles is a web proxy (HTTP Proxy / HTTP Monitor) that runs on your own computer. Your web browser (or any other Internet application) is then configured to access the Internet through Charles, and Charles is then able to record and display for you all of the data that is sent and received.</span>
  </a><a class="result" href="/sqreen">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7904/uUQKRitV_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Sqreen</span>
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
    <span class="additional">Sqreen is a security platform that helps engineering team protect their web applications, API and micro-services in real-time. The solution installs with a simple application library and doesn't require engineering resources to operate. Security anomalies triggered are reported with technical context to help engineers fix the code. Ops team can assess the impact of attacks and monitor suspicious user accounts involved.
</span>
  </a><a class="result" href="/amazon-iot">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3918/reinvent-2015-recap_iot.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon IoT</span>
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
    <span class="additional">AWS IoT is a managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices. AWS IoT can support billions of devices and trillions of messages, and can process and route those messages to AWS endpoints and to other devices reliably and securely. With AWS IoT, your applications can keep track of and communicate with all your devices, all the time, even when they aren’t connected.</span>
  </a><a class="result" href="/rasa-nlu">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6138/icon-200x200.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">rasa NLU</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">rasa NLU (Natural Language Understanding) is a tool for intent classification and entity extraction. You can think of rasa NLU as a set of high level APIs for building your own language parser using existing NLP and ML libraries.</span>
  </a><a class="result" href="/hackerone">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1366/be11fd7771e11a0a2e5f26ffb4e9b0d7.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">HackerOne</span>
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
    <span class="additional">Someone has found a potential security issue with your technology. What happens next? Making certain this discovery leads to a positive outcome for everyone involved is crucial. Replacing an antiquated security@ mailbox with the HackerOne platform brings order and control to an otherwise chaotic process.</span>
  </a><a class="result" href="/loader-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/216/4-rbfATJ.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Loader.io</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">22</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Loader.io is a free load testing service that allows you to stress test
your web-apps/apis with thousands of concurrent connections.</span>
  </a><a class="result" href="/firebase-hosting">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6688/m3cEA33V_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Firebase Hosting</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">31</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is production-grade web content hosting for developers. With a single command, you can quickly deploy web apps and serve both static and dynamic content to a global CDN (content delivery network). You can also pair it with Cloud Functions or Cloud Run to build and host microservices.</span>
  </a><a class="result" href="/vue-storefront">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9528/FB_Profile.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Vue Storefront</span>
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
    <span class="additional">Vue Storefront is a standalone PWA storefront for your eCommerce, possible to connect with any eCommerce backend (eg. Magento, Pimcore, Prestashop or Shopware) through the API.</span>
  </a><a class="result" href="/saleor">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9843/m9Hu1f9G_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Saleor</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Saleor is a rapidly-growing open source e-commerce platform that has served high-volume companies from branches like publishing and apparel since 2012. Based on Python and Django, the latest major update introduces a modular front end powered by a GraphQL API and written with React and TypeScript.</span>
  </a><a class="result" href="/predictionio">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/961/3db97f269b32b0fe3da53abc99f8d91e.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PredictionIO</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">PredictionIO is an open source machine learning server for software developers to create predictive features, such as personalization, recommendation and content discovery.</span>
  </a><a class="result" href="/nltk">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/no-img-open-source.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">NLTK</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">20</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language.</span>
  </a><a class="result" href="/stormpath">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/268/t1WzGozA.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Stormpath</span>
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
    <span class="additional">Stormpath is an authentication and user management service that helps development teams quickly and securely build web and mobile applications and services. </span>
  </a><a class="result" href="/api-blueprint">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5627/Q84Qf_4w.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">API Blueprint</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">35</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">API Blueprint is simple and accessible to everybody involved in the API lifecycle. Its syntax is concise yet expressive. With API Blueprint you can quickly design and prototype APIs to be created or document and test already deployed mission-critical APIs.</span>
  </a><a class="result" href="/material">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4459/material.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Material</span>
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
    <span class="additional">Express your creativity with Material, an animation and graphics framework for Google's Material Design and Apple's Flat UI in Swift.</span>
  </a><a class="result" href="/apache-solr">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4483/apache-solr.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apache Solr</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">19</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It uses the tools you use to make application building a snap. It is built on the battle-tested Apache Zookeeper, it makes it easy to scale up and down.</span>
  </a><a class="result" href="/shields">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/960/l_GA8FC8.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Shields.io</span>
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
    <span class="additional">Legible &amp; concise status badges for third-party codebase services.</span>
  </a><a class="result" href="/spree">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1098/6G46CP-7.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Spree</span>
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
    <span class="additional">The Spree storefront offers a full feature set and is built on common standards, so you don't have to compromise speed to market, efficiency or innovation. The modular platform allows you to easily configure, supplement or replace any functionality you need, so that you can build the exact storefront that you want.</span>
  </a><a class="result" href="/embedly">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/229/1d289aab136f2d111387a399f3a91b6a.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Embedly</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">29</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Embed- Get the world’s most powerful tool for embedding videos, photos, and rich media into websites. Extract- Use the elements—colors, text, keywords, and entities—that you want from articles. Discard the rest automatically. Display- Use the elements—colors, text, keywords, and entities—that you want from articles. Discard the rest automatically.Make the images you use look great—and display quickly—on any screen, every time.</span>
  </a><a class="result" href="/openldap">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5225/zPH8xLZQ_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OpenLDAP</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">17</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a free, open-source implementation of the Lightweight Directory Access Protocol. Lightweight Directory Access is an application protocol that is used to crosscheck information on the server end.</span>
  </a><a class="result" href="/dropbox-paper">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4146/PQ23AUmr_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Dropbox Paper</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">17</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is more than a doc, it’s a workspace that brings creation and coordination together in one place. You can write together, share comments, embed images, and more. If you have a Dropbox account, you can use Paper for free.</span>
  </a><a class="result" href="/alamofire">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5182/XEfzbPga_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Alamofire</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">21</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a Swift-based HTTP networking library for iOS and macOS. It provides an elegant interface on top of Apple's Foundation networking stack that simplifies a number of common networking tasks.</span>
  </a><a class="result" href="/blazemeter">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/498/WYl4LlbI.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">BlazeMeter</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">10</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Simulate any user scenario for webapps, websites, mobile apps or web services. 100% Apache JMeter compatible. Scalable from 1 to 1,000,000+ concurrent users.</span>
  </a><a class="result" href="/1-1">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/41/cca9febe94dd9eccbf4edd7677f79f9c.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">1&amp;1</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">As a recognized partner of VeriSign®, WebSite.ws, ICANN and more; we make domain name registration simple and seamless. Launch your next web project with 1&amp;1 today!</span>
  </a><a class="result" href="/apigility">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2627/eed79f8989d03cd3ce30757f91926287.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apigility</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">An API-based architecture is essential to agile delivery of mobile applications. Apigility provides JSON representations that can be parsed and used in any mobile framework; write for the web or native applications simultaneously!</span>
  </a><a class="result" href="/caffe2">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6821/13072719.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Caffe2</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Caffe2 is deployed at Facebook to help developers and researchers train large machine learning models and deliver AI-powered experiences in our mobile apps. Now, developers will have access to many of the same tools, allowing them to run large-scale distributed training scenarios and build machine learning applications for mobile.</span>
  </a><a class="result" href="/transifex">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/532/15f89f25dd063cb989e3655529ffa321.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Transifex</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">43</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Transifex is a cloud-based localization platform built to help you manage the translation and localization of your app, website, video subtitles, and more. It acts as a repository for your content (think GitHub for translation) and includes tools for developers to get that content into Transifex automatically. Transifex also provides translators a web interface to submit translations. </span>
  </a><a class="result" href="/fiddler">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5319/JMsyvkiF_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Fiddler</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">15</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a free web debugging proxy for any browser, system or platform. It helps you debug web applications by capturing network traffic between the Internet and test computers. The tool enables you to inspect incoming and outgoing data to monitor and modify requests and responses before the browser receives them.</span>
  </a><a class="result" href="/google-cloud-endpoints">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1647/google-cloud-endpoints.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Cloud Endpoints</span>
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
    <span class="additional">An NGINX-based proxy and distributed architecture give unparalleled performance and scalability. Using an Open API Specification or one of our API frameworks, Cloud Endpoints gives you the tools you need for every phase of API development and provides insight with Google Cloud Monitoring, Cloud Trace, Google Cloud Logging and Cloud Trace.</span>
  </a><a class="result" href="/smartsheet">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5067/4_8B8Dg3_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Smartsheet</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an intuitive online project management tool enabling teams to increase productivity using cloud, collaboration, &amp; mobile technologies. It provides your organization with a powerful work platform that offers exceptional speed to business value</span>
  </a><a class="result" href="/prerender">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2533/G8eeH0Ar.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Prerender</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">21</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Search engines and social networks are always trying to crawl your pages, but they only see the javascript tags...We render your javascript in a browser, save the static HTML, and you return that to the crawlers!</span>
  </a><a class="result" href="/arcgis">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4379/mjImnOJe_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ArcGIS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">9</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a geographic information system for working with maps and geographic information. It is used for creating and using maps, compiling geographic data, analyzing mapped information, sharing  and much more.</span>
  </a><a class="result" href="/mashape">
    <div style="display:inline-block">
      <img src="https://ucarecdn.com/274d1d51-138b-432b-b50b-d61bef011d83/">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mashape</span>
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
    <span class="additional">Kong is a scalable, open source API Layer (also known as an API Gateway, or API Middleware). Kong controls layer 4 and 7 traffic and is extended through Plugins, which provide extra functionality and services beyond the core platform.</span>
  </a><a class="result" href="/hyper-terminal">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6489/hyper-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Hyper Terminal</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The goal of the project is to create a beautiful and extensible experience for command-line interface users, built on open web standards. Focus will be primarily around speed and stability.</span>
  </a><a class="result" href="/import-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/966/xuc8kDu_.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">import.io</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">0</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">import.io is a free web-based platform that puts the power of the machine readable web in your hands. Using our tools you can create an API or crawl an entire website in a fraction of the time of traditional methods, no coding required.</span>
  </a><a class="result" href="/crowdin">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/692/Ug8TZcdB_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Crowdin</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">14</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Crowdin is a localization management platform with all the features you need for agile localization. Get your app, game, web app, software and on fast and seamlessly translated into more than 300 languages.</span>
  </a><a class="result" href="/amazon-elastic-inference">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/10045/FrshWMKt_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon Elastic Inference</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon Elastic Inference allows you to attach low-cost GPU-powered acceleration to Amazon EC2 and Amazon SageMaker instances to reduce the cost of running deep learning inference by up to 75%. Amazon Elastic Inference supports TensorFlow, Apache MXNet, and ONNX models, with more frameworks coming soon.</span>
  </a><a class="result" href="/origami">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/873/M0yxswTJ.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Origami</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Origami is a free toolkit for Quartz Composer—created by the Facebook Design team—that makes interactive design prototyping easy and doesn’t require programming.</span>
  </a><a class="result" href="/oauth-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1298/d190fab5c1e28e4a01d9c18604e9f7e0.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OAuth.io</span>
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
    <span class="additional">OAuth is a protocol that aimed to provide a single secure recipe to manage authorizations. It is now used by almost every web application. However, 30+ different implementations coexist. OAuth.io fixes this massive problem by acting as a universal adapter, thanks to a robust API. With OAuth.io integrating OAuth takes minutes instead of hours or days.</span>
  </a><a class="result" href="/google-cloud-natural-language-api">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5515/sf2x8byZ.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Cloud Natural Language API</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">You can use it to extract information about people, places, events and much more, mentioned in text documents, news articles or blog posts. You can use it to understand sentiment about your product on social media or parse intent from customer conversations happening in a call center or a messaging app. You can analyze text uploaded in your request or integrate with your document storage on Google Cloud Storage.</span>
  </a><a class="result" href="/mkdocs">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3415/h4nqPazl_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">MkDocs</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">9</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It builds completely static HTML sites that you can host on GitHub pages, Amazon S3, or anywhere else you choose. There's a stack of good looking themes available. The built-in dev-server allows you to preview your documentation as you're writing it. It will even auto-reload and refresh your browser whenever you save your changes.</span>
  </a><a class="result" href="/react-static">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7731/517937d8-2946-4365-9383-58be0dd1c2f7.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">React-Static</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">React-Static is a next-gen static site generator for React. Finally, you can build a website like you do any other React App. There's no special CMS, query language, or crazy lifecycle hooks. Just good old React producing an amazing SEO-ready, user experience driven, progressively enhanced website. The effort is minimal, but the benefits are not!</span>
  </a><a class="result" href="/falcor">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3461/mHp7LcQN.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Falcor</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Falcor lets you represent all your remote data sources as a single domain model via a virtual JSON graph. You code the same way no matter where the data is, whether in memory on the client or over the network on the server.</span>
  </a><a class="result" href="/tyk-cloud">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2961/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Tyk Cloud</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">10</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Tyk is a lightweight, open source API Gateway and enables you to control who accesses your API, when they access it and how they access it. Tyk will also record detailed analytics on how your users are interacting with your API and when things go wrong.</span>
  </a><a class="result" href="/shopware">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6322/B2Nv76RQ_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Shopware</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">46</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is an eCommerce platform to power your online business. It promotes openness and accessibility which is reflected in its business culture and people. </span>
  </a><a class="result" href="/usertesting">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1132/U_Logo_BrandBlue.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">UserTesting</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">17</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">UserTesting provides on-demand usability testing. You create the test and we’ll get the testers. We let you “look over the shoulder” of your target audience while they use your website, so you can see and hear where users get stuck and why they leave.</span>
  </a><a class="result" href="/amazon-comprehend">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7990/amazon-comprehend.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon Comprehend</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">10</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to discover insights from text. Amazon Comprehend provides Keyphrase Extraction, Sentiment Analysis, Entity Recognition, Topic Modeling, and Language Detection APIs so you can easily integrate natural language processing into your applications.</span>
  </a><a class="result" href="/openface">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/no-img-open-source.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OpenFace</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">OpenFace is a Python and Torch implementation of face recognition with deep neural networks and is based on the CVPR 2015 paper FaceNet: A Unified Embedding for Face Recognition and Clustering by Florian Schroff, Dmitry Kalenichenko, and James Philbin at Google.</span>
  </a><a class="result" href="/ludwig-2">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/10368/ludwig.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Ludwig</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Ludwig is a toolbox built on top of TensorFlow that allows to train and test deep learning models without the need to write code. All you need to provide is a CSV file containing your data, a list of columns to use as inputs, and a list of columns to use as outputs, Ludwig will do the rest.</span>
  </a><a class="result" href="/algorithms-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/309/81af555beec9700f7f10ae97fc9efff2.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Algorithms.io</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Build And Run Predictive Applications For Streaming Data From Applications, Devices, Machines and Wearables</span>
  </a><a class="result" href="/3scale">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1251/20mNxTmx.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">3scale</span>
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
    <span class="additional">3scale's API Management platform provides services and solutions, allowing you to Operate, Manage and Distribute your APIs. Trusted by 450+ API programs.</span>
  </a><a class="result" href="/octopress">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1115/octopress-avatar.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Octopress</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">9</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Octopress is an obsessively designed framework for Jekyll blogging. It’s easy to configure and easy to deploy. </span>
  </a><a class="result" href="/okhttp">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/no-img-open-source.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OkHttp</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">HTTP is the way modern applications network. It’s how we exchange data &amp; media. Doing HTTP efficiently makes your stuff load faster and saves bandwidth.</span>
  </a><a class="result" href="/openssh">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3092/preview.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OpenSSH</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">20</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is the premier connectivity tool for remote login with the SSH protocol. It encrypts all traffic to eliminate eavesdropping, connection hijacking, and other attacks. In addition, OpenSSH provides a large suite of secure tunneling capabilities, several authentication methods, and sophisticated configuration options.</span>
  </a><a class="result" href="/fullcontact">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1291/fc2019-logo-mark_2x.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">FullContact</span>
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
    <span class="additional">FullContact offers developers powerful contact management APIs to you turn partial contact information into full contact data. Query by email, phone, or company domain and receive rich company data in response.</span>
  </a><a class="result" href="/api-umbrella">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/no-img-open-source.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">API Umbrella</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">API Umbrella is a proxy that sits in front of your APIs.
It can seamlessly add common functionality like api keys, rate limiting, and analytics to any API.</span>
  </a><a class="result" href="/phrase">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/511/PHRASE_LOGO_SM_400X400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Phrase</span>
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
    <span class="additional">Translation management solution for web and mobile applications. Collaborate with your team, find professional translators and stay on top of the process.</span>
  </a><a class="result" href="/carto">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2164/carto-logo.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">CARTO</span>
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
    <span class="additional">The CARTO platform empowers everyone, from business analysts to data scientists, to turn location data into business outcomes. We accelerate innovation, power new use cases and disrupt business models through Location Intelligence.</span>
  </a><a class="result" href="/pipelines">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9841/no-img.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Pipelines</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Kubeflow is a machine learning (ML) toolkit that is dedicated to making deployments of ML workflows on Kubernetes simple, portable, and scalable. Kubeflow pipelines are reusable end-to-end ML workflows built using the Kubeflow Pipelines SDK.</span>
  </a><a class="result" href="/aerosolve">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3131/aerosolve2.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Aerosolve</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">This library is meant to be used with sparse, interpretable features such as those that commonly occur in search (search keywords, filters) or pricing (number of rooms, location, price). It is not as interpretable with problems with very dense non-human interpretable features such as raw pixels or audio samples.</span>
  </a><a class="result" href="/amazon-swf">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/394/16ffae8c667bdbc6a4969f6f02090652.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Amazon SWF</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">13</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Amazon Simple Workflow allows you to structure the various processing steps in an application that runs across one or more machines as a set of “tasks.” Amazon SWF manages dependencies between the tasks, schedules the tasks for execution, and runs any logic that needs to be executed in parallel. The service also stores the tasks, reliably dispatches them to application components, tracks their progress, and keeps their latest state.</span>
  </a><a class="result" href="/castle">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4394/gFD3SSJB.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Castle</span>
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
    <span class="additional">Castle looks for suspicious login patterns without bothering the legitimate user nor the site administrator. The fully-automated anti-hijack engine identifies potential account compromises based on where the user logs in from and how they navigate the site.</span>
  </a><a class="result" href="/wufoo">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/93/_CNk3Tbx.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Wufoo</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">10</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Wufoo automatically builds the database, backend and scripts needed to make collecting and understanding your data easy, fast and fun. Because we host everything, all you need is a browser, an Internet connection and a few minutes to build a form and start using it right away.</span>
  </a><a class="result" href="/sso-buzzfeed">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9493/sso.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">sso</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The authentication and authorization system BuzzFeed developed to provide a secure, single sign-on experience for access to the many internal web apps used by our employees.</span>
  </a><a class="result" href="/deployd">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2521/logo-no-text.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Deployd</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Deployd is the simplest way to build realtime APIs for web and mobile apps. Ready-made, configurable Resources add common functionality to a Deployd backend, which can be further customized with JavaScript Events.</span>
  </a><a class="result" href="/programmableweb">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/513/7Y4K_YPl.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">ProgrammableWeb</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">ProgrammableWeb is more than a directory and community, it's programmable. Our "API for APIs" gives you a simple and structured way to access the powerful registry and repository capabilities of PW. Use your favorite language to search and retrieve APIs, mashups, and other data from our catalog. We've got samples in PHP, Java, .NET and JavaScript to get you started.</span>
  </a><a class="result" href="/beautifulsoup">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4037/no-img-open-source.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">BeautifulSoup</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.</span>
  </a><a class="result" href="/onenote">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7626/ikCJDPLz_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">OneNote</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">7</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Get organized in notebooks you can divide into sections and pages. With easy navigation and search, you’ll always find your notes right where you left them. It gathers users' notes, drawings, screen clippings and audio commentaries. Notes can be shared with other OneNote users over the Internet or a network. </span>
  </a><a class="result" href="/theano">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6241/theano.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Theano</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Theano is a Python library that lets you to define, optimize, and evaluate mathematical expressions, especially ones with multi-dimensional arrays (numpy.ndarray). Using Theano it is possible to attain speeds rivaling hand-crafted C impleme</span>
  </a><a class="result" href="/aws-iot-device-management">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7996/aws-iot_20copy.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS IoT Device Management</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AWS IoT Device Management makes it easy to securely onboard, organize, monitor, and remotely manage IoT devices at scale. IoT Device Management lets you register your devices individually or in bulk, and manage permissions so that devices remain secure. Then, you use the IoT Device Management console to organize your devices into groups, monitor and troubleshoot device functionality, and send remote updates to your devices. </span>
  </a><a class="result" href="/gluon">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7729/gluon-api.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gluon</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">0</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A new open source deep learning interface which allows developers to more easily and quickly build machine learning models, without compromising performance. Gluon provides a clear, concise API for defining machine learning models using a collection of pre-built, optimized neural network components.</span>
  </a><a class="result" href="/gelato-io">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3258/4sYR50d5.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Gelato.io</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Gelato.io is a SaaS tool for creating API documentation and developer portals. </span>
  </a><a class="result" href="/mxnet">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8352/kxyKWxfA_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">MXNet</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">5</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A deep learning framework designed for both efficiency and flexibility. It allows you to mix symbolic and imperative programming to maximize efficiency and productivity. At its core, it contains a dynamic dependency scheduler that automatically parallelizes both symbolic and imperative operations on the fly.</span>
  </a><a class="result" href="/11ty">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/9640/8ZfcJCXi_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">11ty</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">A simpler static site generator. An alternative to Jekyll. Written in JavaScript. Transforms a directory of templates (of varying types) into HTML.

Works with HTML, Markdown, Liquid, Nunjucks, Handlebars, Mustache, EJS, Haml, Pug, and JavaScript Template Literals.</span>
  </a><a class="result" href="/caffe">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5557/New_Project__83_.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Caffe</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a deep learning framework made with expression, speed, and modularity in mind.</span>
  </a><a class="result" href="/fiber">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7400/ZnsBwsIu_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Fiber</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Fiber UI Kit is the perfect starting place for your next project. Each element has been designed to work independently or as one seamless flow. It’s a full-fledged prototype with customizable components.</span>
  </a><a class="result" href="/aws-shield">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6087/16ffae8c667bdbc6a4969f6f02090652.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS Shield</span>
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
    <span class="additional">AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards web applications running on AWS. AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency, so there is no need to engage AWS Support to benefit from DDoS protection.</span>
  </a><a class="result" href="/restlet-studio">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2506/2mSsFFsG.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Restlet Studio</span>
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
    <span class="additional">Packaged as a Chrome extension and accessible from any modern web browser, Restlet Studio instantly provides to any developer powerful API crafting capabilities. Through an intuitive interface, developers can visually define all the elements of a web API, and automatically generate the client SDK and server skeleton of their API.</span>
  </a><a class="result" href="/apifier">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3973/PYBKS1GX.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Apifier</span>
        <span class="fa fa-check-circle"></span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Apifier is a hosted web crawler for developers that enables them to extract data from any website using a few simple lines of JavaScript and rapidly build new apps on top of existing third-party web apps and data sources.</span>
  </a><a class="result" href="/portia">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4465/M510KmGH.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Portia</span>
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
    <span class="additional">Portia is an open source tool that lets you get data from websites. It facilitates and automates the process of data extraction. This visual web scraper works straight from your browser, so you don't need to download or install anything.</span>
  </a><a class="result" href="/tilda">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/8122/FOiPb6qs_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Tilda</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">33</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a website builder that can be used to create websites, landing pages, online stores and special projects.</span>
  </a><a class="result" href="/aws-direct-connect">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/425/aws-direct-connect.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS Direct Connect</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">13</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">AWS Direct Connect makes it easy to establish a dedicated network connection from your premises to AWS. Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office, or colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections. </span>
  </a><a class="result" href="/bing-maps-api">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1102/Sgv8z7DN.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bing Maps API</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The Bing Maps platform provides multiple API options for your application including Web Control, a Windows Store apps control, a WPF control, REST Services, and Spatial Data Services. Use the information below as well as at MSDN to help determine which API bests suits your needs.</span>
  </a><a class="result" href="/bugcrowd">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/746/2b0f47cc51770f0a0c83f78cb79689ad.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bugcrowd</span>
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
    <span class="additional">Our Crowdcontrol platform safely connects you to a curated community of 8,300 security researchers to securely capture, triage and reward vulnerabilities in your code. Reduce your effort by over 85% and get back to work!</span>
  </a><a class="result" href="/google-keep">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5598/New_Project__4_.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Keep</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a note-taking service developed by Google. It is available on the web, and has mobile apps for the Android and iOS mobile operating systems. Keep offers a variety of tools for taking notes, including text, lists, images, and audio.</span>
  </a><a class="result" href="/iwantmyname">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/39/4c4e092f93988573baef04a18f7d1e2a.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">iwantmyname</span>
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
    <span class="additional">With iwantmyname, you can purchase 250+ international domain extensions and easily connect your web addresses to the best apps and services on the web, including Google Apps, Squarespace, Bitly, and Ghost. </span>
  </a><a class="result" href="/google-forms">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2879/Google_Forms_Logo.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Google Forms</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">6</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a cloud-based questionnaire and survey solution with real-time collaboration and powerful tools to customize form questions. It can also be used to create online quizzes.</span>
  </a><a class="result" href="/000webhost">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5267/k1SrAvnA_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">000webhost</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Free Web Hosting with PHP, MySQL, free Website Builder, cPanel and no ads. Almost unlimited free website hosting and free domain hosting.</span>
  </a><a class="result" href="/livefyre">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/30/nmo0BfUa.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">LiveFyre</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">32</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Livefyre’s real-time apps get your audience talking and turn your site into the hub for your community. Bloggers, brands and the largest publishers in the world use Livefyre to engage their users and curate live content from around the social web.</span>
  </a><a class="result" href="/nanonets">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6713/logo_blue3_copy_2.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">NanoNets</span>
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
    <span class="additional">Build a custom machine learning model without expertise or large amount of data. Just go to nanonets, upload images, wait for few minutes and integrate nanonets API to your application.</span>
  </a><a class="result" href="/supernova">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7595/KgrG0TVq_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Supernova</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">0</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Supernova converts any mobile design to full-fledged native applications, giving the developers extra time to do actual coding. No need to export resources, write navigation, connect it to components created by hand, read styles, apply styles, copy-paste information..</span>
  </a><a class="result" href="/maps-me">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3734/Q75eOFNM.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">MAPS.ME</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">0</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">MAPS.ME is an open source cross-platform offline maps application, built on top of crowd-sourced OpenStreetMap data. It was publicly released for iOS and Android.</span>
  </a><a class="result" href="/bonsai">
    <div style="display:inline-block">
      <img src="https://ucarecdn.com/6fe49314-ff9d-4ebd-913d-ff1bb3c70304/">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Bonsai</span>
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
    <span class="additional">Your customers expect fast, near-magical results from your  search. Help them find what they’re looking for with Bonsai Elasticsearch. Our fully managed Elasticsearch solution makes it easy to create, manage, and test your app's search.</span>
  </a><a class="result" href="/detectify">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4059/looVYp5o_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Detectify</span>
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
    <span class="additional">Detectify is a web security service that simulates automated hacker attacks on your website, detecting critical security issues before real hackers do. We provide you with descriptive reports of the results so that you can continue to build safe products</span>
  </a><a class="result" href="/easypost">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/280/07bef5ea57ce92dd3e19f47304c14e27.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">EasyPost</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">9</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Add shipping APIs to your application in minutes instead of weeks. Get the best shipping rates by unlocking every major carrier in one simple integration.</span>
  </a><a class="result" href="/walkme">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/169/em4ejlmbqukcn0mdm4sc.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">WalkMe</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">WalkMe enables website owners and app developers to easily create multiple interactive on-screen Walk-Thru’s that help users to quickly and easily complete even the most complex tasks.</span>
  </a><a class="result" href="/divshot">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/684/cHBIc-SE.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Divshot</span>
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
    <span class="additional">Divshot makes building and hosting front-end web applications simple. Build locally and deploy using a simple command-line interface. Divshot supports multiple environments, pushState routing, atomic deploys, and more.</span>
  </a><a class="result" href="/flinto">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1931/LnYdLVHE_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Flinto</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">12</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It is a Mac app used by designers around the world to create interactive and animated prototypes of their app designs. It lets designers quickly make interactive prototypes of their mobile, desktop, or web apps.</span>
  </a><a class="result" href="/microsoft-cognitive-services">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7151/mscognitive.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Microsoft Cognitive Services</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">18</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Infuse your apps, websites and bots with intelligent algorithms to see, hear, speak, understand and interpret your user needs through natural methods of communication. Transform your business with AI today.</span>
  </a><a class="result" href="/aws-greengrass">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7092/Screen-Shot-2017-06-16-at-3.12.18-PM.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS Greengrass</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">2</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Greengrass lets you run IoT applications seamlessly across the AWS cloud and local devices using AWS Lambda and AWS IoT.</span>
  </a><a class="result" href="/docsify">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/7055/docsify.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Docsify</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Docsify generates your documentation website on the fly without generating static html files. Instead, it loads and parses your Markdown files and displays them as a website.</span>
  </a><a class="result" href="/cronofy">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/2295/7dFmNVCA.jpeg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Cronofy</span>
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
    <span class="additional">Real-time scheduling API and UI to delivery embedded scheduling in SaaS applications.</span>
  </a><a class="result" href="/mirage">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/5824/mirage.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Mirage</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The Elasticsearch query DSL supports 100+ query APIs ranging from full-text search, numeric range filters, geolocation queries to nested and span queries. Mirage is a modern, open-source web based query explorer for Elasticsearch.</span>
  </a><a class="result" href="/aws-storage-gateway">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/413/aws-storage-gateway.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">AWS Storage Gateway</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">The AWS Storage Gateway is a service connecting an on-premises software appliance with cloud-based storage. Once the AWS Storage Gateway’s software appliance is installed on a local host, you can mount Storage Gateway volumes to your on-premises application servers as iSCSI devices, enabling a wide variety of systems and applications to make use of them. Data written to these volumes is maintained on your on-premises storage hardware while being asynchronously backed up to AWS, where it is stored in Amazon Glacier or in Amazon S3 in the form of Amazon EBS snapshots. Snapshots are encrypted to make sure that customers do not have to worry about encrypting sensitive data themselves. When customers need to retrieve data, they can restore snapshots locally, or create Amazon EBS volumes from snapshots for use with applications running in Amazon EC2. It provides low-latency performance by maintaining frequently accessed data on-premises while securely storing all of your data encrypted.</span>
  </a><a class="result" href="/ns1">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/3454/JNM4JQf.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">NS1</span>
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
    <span class="additional">NS1’s intelligent DNS &amp; traffic management platform, with its data driven architecture and unique Filter Chain routing engine, is purpose-built for the most demanding, mission-critical applications on the Internet.</span>
  </a><a class="result" href="/dejavu">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/4686/icon.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Dejavu</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">1</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">dejaVu fits the unmet need of being a hackable data browser for Elasticsearch. Existing browsers were either built with a legacy UI and had a lacking user experience or used server side rendering (I am looking at you, Kibana).</span>
  </a><a class="result" href="/formstack">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/94/5LccSImE_400x400.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Formstack</span>
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
    <span class="additional">Formstack is an online form building application that lets you bring your forms online without any coding knowledge. The Formstack drag and drop form builder lets you build custom forms and easily collect data in your Formstack database.</span>
  </a><a class="result" href="/osquery">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6949/68747470733a2f2f6f7371756572792e696f2f6173736574732f6c6f676f2d6461726b2e706e67.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">osquery</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">3</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">osquery exposes an operating system as a high-performance relational database. This allows you to write SQL-based queries to explore operating system data. With osquery, SQL tables represent abstract concepts such as running processes, loaded kernel modules, open network connections, browser plugins, hardware events or file hashes.</span>
  </a><a class="result" href="/asciinema">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1135/5Pz7-WC6.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Asciinema</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">4</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Asciinema is a free and open source solution for recording the terminal sessions and sharing them on the web.</span>
  </a><a class="result" href="/kur">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/6566/XoM66m5U.png">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">Kur</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">0</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">Kur is a system for quickly building and applying state-of-the-art deep learning models to new and exciting problems. Kur was designed to appeal to the entire machine learning community, from novices to veterans.</span>
  </a><a class="result" href="/powerdns">
    <div style="display:inline-block">
      <img src="https://img.stackshare.io/service/1704/mt4rn9iC_400x400.jpg">
      <span class="type-label">Tool</span>
    </div>
    <div style="display: inline-block;vertical-align: top;">
      <span class="additional-name">PowerDNS</span>
      <span class="hint--top" data-align="left" data-hint="Stacks including this">
        <span class="glyphicon glyphicon-align-justify"></span>
        <span class="count-search">13</span>
      </span>
      <span class="hint--top" data-align="left" data-hint="Votes">
        <span class="octicon octicon-arrow-up"></span>
        <span class="count-search"></span>
      </span>
    </div>
    <span class="additional">It features a large number of different backends ranging from simple BIND style zonefiles to relational databases and load balancing/failover algorithms. A DNS recursor is provided as a separate program.</span>
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
data.to_csv('C:/Users/i9i91/OneDrive/바탕 화면/github 저장내용/portfolio.io/크롤링2.csv')  




