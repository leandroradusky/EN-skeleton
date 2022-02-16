import { writable } from 'svelte/store'

const filtersStore = () => {
  const getEmptyStore = () => ({
    shownVar: '',
  })

  const { subscribe, set, update: _update } = writable(getEmptyStore())

  let state
  subscribe((_state) => {
    state = _state
  })

  const update = (fn) => {
    _update(fn)

    // Update url query params
    const url = new URL(window.location.href)
    Object.keys(state)
      .filter((key) => key !== 'hover')
      .forEach((key) => {
        if (state[key]) url.searchParams.set(key, state[key])
        else url.searchParams.delete(key)
      })
    window.history.pushState({ path: url.toString() }, '', url.toString())
  }

  const setShownVar = (val) => {
    if (val !== state.shownVar) update((state) => ({ ...state, shownVar: val }))
  }

  return {
    subscribe,
    update,
    set,
    setShownVar,
  }
}

export const filters = filtersStore()
