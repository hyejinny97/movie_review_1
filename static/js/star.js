const star_point = document.querySelector('#star_point')
const star_rates = document.querySelectorAll('.star-rate')

for (let star_rate of star_rates) {
  if (star_rate.defaultValue == star_point.value) {
    star_rate.setAttribute('checked', true)
  }
}