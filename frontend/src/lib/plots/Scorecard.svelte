<script>
  export let id = 'scorecard'
  export let heading
  export let score
</script>

<div class="scorecard">
  <div class="heading">{heading}</div>
  <div class="score">{score}</div>
</div>

<style lang="scss">
  .scorecard {
    width: 100%;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
    overflow: hidden;
  }
  .heading {
    padding-top: 10%;
    text-align: center;
    font-size: 16px;
    color: #999;
  }
  .score {
    text-align: center;
    font-size: 36px;
    padding-bottom: 10%;
    padding-top: 5%;
  }
</style>
