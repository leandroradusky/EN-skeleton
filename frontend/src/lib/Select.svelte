<script>
  export let options = []
  export let selected = {}
  export let change = (newValue) => {}

  let select
  let isOpen = false

  const handleClose = ({ target }) => {
    if (!select.contains(target)) isOpen = false
  }

  const handleClickOpt = (opt) => {
    isOpen = false
    selected = opt
    change(opt)
  }
</script>

<svelte:body on:click={handleClose} />
<div>
  <label id="listbox-label" class="block text-sm font-medium text-gray-700">
    Assigned to
  </label>
  <div bind:this={select} class="mt-1 relative">
    <button
      type="button"
      class="relative w-full bg-white border border-gray-300 rounded-md shadow-sm pl-3 pr-10 py-2 text-left cursor-default focus:outline-none focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
      aria-haspopup="listbox"
      aria-expanded="true"
      aria-labelledby="listbox-label"
      on:click={() => {
        isOpen = !isOpen
      }}
    >
      <span class="block truncate">
        {selected.label}
      </span>
      <span
        class="ml-3 absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none"
      >
        <!-- Heroicon name: solid/selector -->
        <svg
          class="h-5 w-5 text-gray-400"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
        >
          <path
            fill-rule="evenodd"
            d="M10 3a1 1 0 01.707.293l3 3a1 1 0 01-1.414 1.414L10 5.414 7.707 7.707a1 1 0 01-1.414-1.414l3-3A1 1 0 0110 3zm-3.707 9.293a1 1 0 011.414 0L10 14.586l2.293-2.293a1 1 0 011.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z"
            clip-rule="evenodd"
          />
        </svg>
      </span>
    </button>

    <ul
      class="absolute z-10 mt-1 w-full bg-white shadow-lg max-h-56 rounded-md py-1 text-base ring-1 ring-black ring-opacity-5 overflow-auto focus:outline-none sm:text-sm"
      class:hidden={!isOpen}
      tabindex="-1"
      role="listbox"
      aria-labelledby="listbox-label"
      aria-activedescendant="listbox-option-3"
    >
      {#each options as opt}
        <li
          class="text-gray-900 cursor-default select-none relative py-2 pl-3 pr-9 hover:text-white hover:bg-indigo-600"
          role="option"
          on:click={handleClickOpt(opt)}
        >
          {opt.label}

          {#if opt.value === selected.value}
            <span
              class="text-indigo-600 absolute inset-y-0 right-0 flex items-center pr-4"
            >
              <!-- Heroicon name: solid/check -->
              <svg
                class="h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                  clip-rule="evenodd"
                />
              </svg>
            </span>
          {/if}
        </li>
      {/each}
    </ul>
  </div>
</div>

<style lang="scss">
  li:hover {
    span {
      @apply text-white;
    }
  }
</style>
