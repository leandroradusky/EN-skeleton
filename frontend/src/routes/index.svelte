<script>
  import { onMount } from 'svelte'
  import { getData } from '$lib/utils'
  import Scorecard from '../lib/plots/Scorecard.svelte'
  import Lineplot from '../lib/plots/Lineplot.svelte'

  import * as d3 from 'd3'

  let data
  let leftLineplotData
  let rightLineplotData

  const parse = d3.utcFormat('%B %d, %Y')

  // For select
  const options = [
    {
      label: 'Covid19 cases',
      value: 'cases',
    },
    {
      label: 'Covid19 deaths',
      value: 'deaths',
    },
  ]
  let selectedVar = options[0].value
  let selectedLabel = options[0].label
  let unselectedVar = options[1].value
  let unselectedLabel = options[1].label

  const change = async (e) => {
    selectedVar = e.target.value
    setChartData()
  }

  const setChartData = async () => {
    unselectedVar =
      selectedVar === options[0].value ? options[1].value : options[0].value
    unselectedLabel =
      selectedVar === options[0].value ? options[1].label : options[0].label
    selectedLabel =
      selectedVar === options[0].value ? options[0].label : options[1].value

    leftLineplotData = data[selectedVar]
    rightLineplotData = data[unselectedVar]
  }

  onMount(async () => {
    data = await getData()
    setChartData()
    return
  })
</script>

<header>
  <h1>Hello <strong>EN</strong></h1>
  <h2>Welcome to <strong>Exposure Notifications</strong> example dashboard!</h2>
  <br />
  Select the variable you want to display on the left... don't worry, the other will
  display on the right :)
  <br />
  <select id="variable" value={selectedVar} on:change={change}>
    {#each options as option}
      <option value={option.value}>{option.label} </option>
    {/each}
  </select>
</header>

{#if leftLineplotData && rightLineplotData}
  <main>
    <section>
      <div>
        <Scorecard
          id="scorecard1"
          heading="Total {selectedLabel} at {parse(
            new Date(leftLineplotData[0].date)
          )}"
          score={leftLineplotData[0].value}
        />
      </div>
    </section>
    <section>
      <div>
        <Scorecard
          id="scorecard1"
          heading="Total {unselectedLabel} at {parse(
            new Date(rightLineplotData[0].date)
          )}"
          score={rightLineplotData[0].value}
        />
      </div>
    </section>

    <section>
      <div>
        <Lineplot
          id="lineplot"
          data={leftLineplotData}
          shownVars={selectedVar}
        />
      </div>
    </section>
    <section>
      <div>
        <Lineplot
          id="lineplot2"
          data={rightLineplotData}
          shownVars={unselectedVar}
        />
      </div>
    </section>
  </main>
{/if}

<style lang="scss">
  header {
    padding: 3% 10%;
    text-align: center;
  }

  main {
    margin: 48px 0;
    padding: 0 10%;
    display: grid;
    grid-template-columns: 1fr;
    column-gap: 12px;
    row-gap: 12px;

    @include md {
      grid-template-columns: 1fr 1fr;
      column-gap: 48px;
      row-gap: 48px;
    }
  }
  section {
    display: grid;
    grid-template-rows: 1fr;
    align-items: center;
    row-gap: 12px;
  }
</style>
