export const backendUrl =
  process.env.NODE_ENV === 'development'
    ? 'http://localhost:8000'
    : 'https://canotify-stg.instedd.org'

export const getData = async () => {
  let response = await fetch(`${backendUrl}/api/time_serie/cases`)
  let cases = await response.json()

  response = await fetch(`${backendUrl}/api/time_serie/deaths`)
  let deaths = await response.json()

  return { cases: cases, deaths: deaths }
}
