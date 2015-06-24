program integration_test
    use, intrinsic :: iso_fortran_env, only : dp => REAL64, error_unit
    use :: gauss_mod, only : gen_gauss_type
    implicit none
    type(gen_gauss_type) :: quad
    integer :: nr_points, n, i
    real(kind=dp) :: a, b, eps = 1.0e-9_dp, delta = 0.01_dp, total
    character(len=1024) :: buffer

    if (command_argument_count() >= 4) then
        call get_command_argument(1, buffer)
        read (buffer, fmt='(I10)') nr_points
        call get_command_argument(2, buffer)
        read (buffer, fmt='(E25.15)') a
        call get_command_argument(3, buffer)
        read (buffer, fmt='(E25.15)') b
        call get_command_argument(4, buffer)
        read (buffer, fmt='(I10)') n
    else
        write (unit=error_unit, fmt='(A)') &
            '#error: 4 command line argument expected, nr_points, ' // &
            'a, b, and N'
    end if
    call quad%init_gen_gauss(nr_points, eps)
    total = 0.0_dp
    do i = 0, n - 1
        total = total + quad%integrate(f, a + i*delta, b + i*delta)/n
    end do
    print '(F25.15)', total

contains

    function f(x) result(r)
        implicit none
        real(kind=dp), intent(in) :: x
        real(kind=dp) :: r
        r = (cos(x)**2)*exp(-0.37_dp*x**2)/(x**2 + 17.0_dp)
    end function f

end program integration_test
