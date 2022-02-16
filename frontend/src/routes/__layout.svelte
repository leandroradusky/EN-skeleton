<script>
  import '../app.css'

  const description = `You have the power to help your friends,
family and community. Add your phone to California's
exposure notification system to get COVID-19 exposure
alerts and to protect those around you.`

  const faviconUrl =
    (process.env.NODE_ENV === 'development' ? '/' : '/static/') + 'favicon.png'
</script>

<svelte:head>
  <link rel="icon" href={faviconUrl} />
  <title>Hello EN!</title>
  <meta name="description" content={description} />
  <meta property="og:description" content={description} />
  <meta property="og:locale" content="en_US" />
</svelte:head>

<slot />
