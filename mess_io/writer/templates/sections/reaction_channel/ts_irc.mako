Barrier ${ts_label} ${reac_label} ${prod_label}
  Variational
${ts_data}\
## Zero Energy Section
    ZeroEnergy[kcal/mol]      ${zero_energy}
## Tunnel Section
% if tunnel != '':
${tunnel}
% endif
  End
End
