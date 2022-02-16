<script>
  import * as d3 from 'd3'
  import { onMount } from 'svelte'

  export let id
  export let data = []
  export let shownVars = []

  let svg
  let width

  const render = () => {
    if (!data && data.length < 2) return
    const height = width

    svg = d3
      .select(`#${id} svg`)
      .attr('viewBox', [0, 0, width, height + 50])
      .attr('preserveAspectRatio', 'xMidYMin meet')

    const x = d3
      .scaleUtc()
      .domain(d3.extent(data, (d, i) => new Date(d.date)))
      .range([0, width])

    const max = d3.max(data, (d) => d.value)
    const ticks = Math.ceil(Math.log10(max))
    const y = d3
      .scaleSymlog()
      .domain([0, 10 ** ticks])
      .range([height, 0])
    const color = d3
      .scaleOrdinal()
      .domain(Array.from(data.keys()))
      .range(['#333333', 'rgba(0, 0, 0, 0.5)', 'rgba(0, 0, 0, 0.25)'])

    const xAxis = d3.axisBottom(x).ticks(width / 20)

    const tickValues = Array.from({ length: ticks }, (d, i) => 10 ** (i + 1))
    const yAxis = d3
      .axisRight(y)
      .tickValues(tickValues)
      .tickSize(width)
      .tickPadding(-width + 6)

    svg
      .select('.xAxis')
      .call(xAxis)
      .call((g) => {
        g.attr('transform', `translate(0, ${height + 25})`)
        g.selectAll('.domain').remove()
        g.selectAll('.tick line').remove()
        g.selectAll('text')
          .attr('opacity', 0.5)
          .attr('transform', 'rotate(-85)')
      })

    svg
      .select('.yAxis')
      .call(yAxis)
      .call((g) => {
        g.selectAll('.domain').remove()
        g.selectAll('.tick:last-child line').remove()
        g.selectAll('.tick line')
          .attr('shape-rendering', 'crispEdges')
          .attr('opacity', 0.1)
        g.selectAll('text').attr('y', 12).attr('opacity', 0.5)
      })
    svg
      .select('.lines')
      .selectAll('path')
      .data([data])
      .join('path')
      .attr('fill', 'none')
      .attr('stroke-width', 3)
      .attr('stroke-linejoin', 'round')
      .attr('stroke', (d) => color(d[0]))
      .attr('d', (d, i) => {
        return d3
          .line()
          .x((e) => x(new Date(e.date)))
          .y((e) => y(e.value))
          .defined(true)(d)
        //.defined((d) => { console.log(d); return (parseFloat(d.value) >= 0.0 ? true : false) })(d)
      })

    svg.select('.background').attr('width', width).attr('height', height)

    const legends = d3
      .select(`#${id}`)
      .select('.legends')
      .selectAll('.legend')
      .data([shownVars])

    legends
      .enter()
      .append('div')
      .attr('class', 'legend')
      .call((g) => {
        g.append('div')
          .attr('width', '12px')
          .attr('height', '0')
          .style('border-top', (d) => `3px ${color(d[0])} solid`)
        g.append('span')
          .text((d) => d)
          .style('color', (d) => color(d[0]))
      })

    legends.exit().remove()

    legends.select('span').text((d) => d)
  }

  onMount(() => render())
  $: if (data && data.length > 0) render(width)
</script>

<div bind:clientWidth={width} class="lineplot" {id}>
  <svg style="--b: -1px">
    <rect class="background" rx="4" />
    <g class="xAxis" />
    <g class="yAxis" />
    <g class="lines" />
  </svg>
  <div class="legends" />
</div>

<style lang="scss">
  .lineplot {
    align-self: start;
    position: relative;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
    overflow: hidden;
    .background {
      fill: rgba(0, 0, 0, 0.05);
    }
    .legends {
      font-size: 12px;
      position: absolute;
      bottom: 80px;
      right: 18px;
      display: grid;
      grid-auto-flow: column;
      column-gap: 30px;
    }
  }
</style>
